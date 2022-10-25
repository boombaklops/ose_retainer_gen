#made by boombaklops. modify as you please, but gimme credit :)
from random import randint, choice

class Retainer():

    def __init__(self):
        #preparing lists for later use
        races = [
            'Half-Orc',
            'Human'
        ]
        jobs = [
            'Fighter',
            'Thief'
        ]
        one_handed_weapons = [
            'club 1d4',
            'dagger 1d4',
            'hand axe 1d6',
            'javelin 1d4',
            'mace 1d6',
            'short sword 1d6',
            'silver dagger 1d4',
            'sling 1d4',
            'spear 1d6',
            'sword 1d8',
            'war hammer 1d6'
        ]
        two_handed_weapons = [
            'battle axe 1d8',
            'staff 1d4',
            'two-handed sword 1d10',
            'short bow 1d6',
            'polearm 1d10',
            'long bow 1d6',
            'lance 1d6',
            'crossbow 1d6'
        ]
        armor = [
            'leather armor AC 7 [12]',
            'chain armor AC 5 [14]',
            'plate armor AC 3 [16]'
        ]

        #stats
        self.strength = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.intelligence = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.wisdom = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.dexterity = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.constitution = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.charisma = randint(1, 6) + randint(1, 6) + randint(1, 6)

        #race selection
        if self.intelligence >= 9:races.extend(['Drow', 'Elf'])
        if self.intelligence >= 9 and self.constitution >= 9: races.extend(['Duergar', 'Gnome'])
        if self.constitution >= 9: races.extend(['Dwarf', 'Svirfneblin'])
        if self.charisma >= 9 and self.constitution >= 9: races.append('Half-Elf')
        if self.dexterity >= 9 and self.constitution >= 9: races.append('Halfling')
        #choose a race
        self.race = choice(races)

        #modify stats, then class eligibility checks
        if self.race == 'Drow':
            self.constitution -= 1
            self.dexterity += 1
            jobs.extend(["Acrobat","Assassin","Cleric","Magic-User"])
            if self.constitution >= 9 and self.wisdom >= 9: jobs.append("Ranger")
            if self.constitution >= 9 and self.dexterity >= 9: jobs.append("Knight")
        if self.race == 'Duergar':
            self.charisma -= 1
            self.constitution += 1
            jobs.extend(['Assassin', 'Cleric'])
        if self.race == 'Dwarf':
            self.charisma -= 1
            self.constitution += 1
            jobs.extend(['Assassin', 'Cleric'])
        if self.race == 'Elf':
            self.dexterity += 1
            self.constitution -= 1
            jobs.extend(["Acrobat","Assassin","Cleric","Druid","Magic-User"])
            if self.constitution >= 9 and self.dexterity >= 9: jobs.append("Knight")
            if self.constitution >= 9 and self.wisdom >= 9: jobs.append("Ranger")
        if self.race == 'Gnome':
            jobs.extend(["Assassin","Cleric"])
            if self.dexterity >= 9: jobs.append("Illusionist")
        if self.race == 'Half-Elf':
            jobs.extend(["Acrobat","Assassin","Cleric","Magic-User"])
            if self.dexterity >= 9 and self.intelligence >= 9: jobs.append("Bard")
            if self.constitution >= 9 and self.wisdom >= 9: jobs.append("Ranger")
            if self.charisma >= 9: jobs.append("Paladin")
            if self.constitution >= 9 and self.dexterity >= 9: jobs.append("Knight")
        if self.race == 'Halfling':
            self.dexterity += 1
            self.strength -= 1
            jobs.append('Druid')
        if self.race == 'Half-Orc':
            self.constitution += 1
            self.charisma -= 2
            jobs.extend(['Acrobat', 'Assassin', 'Cleric'])
        if self.race ==  'Human':
            jobs.extend(["Acrobat","Assassin","Cleric","Druid","Magic-User"])
            if self.dexterity >= 9 and self.intelligence >= 9: jobs.append("Bard")
            if self.dexterity >= 9: jobs.append("Barbarian")
            if self.constitution >= 9 and self.wisdom >= 9: jobs.append("Ranger")
            if self.charisma >= 9: jobs.append("Paladin")
            if self.constitution >= 9 and self.dexterity >= 9: jobs.append("Knight")
            if self.dexterity >= 9: jobs.append("Illusionist")
        if self.race == 'Svirfneblin':
            jobs.extend(["Assassin","Cleric","Druid","Magic-User"])
        #choose class
        self.job = choice(jobs)

        #job-related generation
        self.inventory = []
        self.spells_known = []
        if self.job == 'Acrobat':
            self.hp = randint(1, 4) + self.get_conmod()
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
            self.inventory.append('leather armor AC 7 [12]')
            self.inventory.append(choice([
                'short bow 1d6',
                'long bow 1d6',
                'crossbow 1d6',
                'dagger 1d4',
                'sword 1d8',
                'short sword 1d6',
                'polearm 1d10',
                'spear 1d6',
                'staff 1d4'
            ]))

        if self.job == 'Assassin':
            self.hp = randint(1, 4) + self.get_conmod()
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Neutral', 'Chaotic'])
            self.inventory.append('leather armor AC 7 [12]')
            weapon = choice(two_handed_weapons + one_handed_weapons)
            self.inventory.append(weapon)
            if weapon not in two_handed_weapons and weapon != 'sling 1d4': self.inventory.append('shield AC +1')

        if self.job == 'Barbarian':
            self.hp = randint(1, 8) + self.get_conmod()
            self.death_save = 10
            self.wand_save = 13
            self.poison_save = 12
            self.breath_save = 15
            self.spell_save = 16
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
            self.inventory.append(choice(['leather armor AC 7 [12]', 'chain armor AC 5 [14]']))
            weapon = choice(two_handed_weapons + one_handed_weapons)
            self.inventory.append(weapon)
            if weapon not in two_handed_weapons and weapon != 'sling 1d4': self.inventory.append('shield AC +1')

        if self.job == 'Bard':
            self.hp = randint(1, 6) + self.get_conmod()
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
            self.inventory.append(choice(['leather armor AC 7 [12]', 'chain armor AC 5 [14]']))
            weapon = choice(['short bow 1d6', 'long bow 1d6', 'crossbow 1d6'] + one_handed_weapons)
            self.inventory.append(weapon)

        if self.job == 'Cleric':
            self.hp = randint(1, 6) + self.get_conmod()
            self.death_save = 11
            self.wand_save = 12
            self.poison_save = 14
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
            self.inventory.append(choice(armor))
            weapon = choice([
            'club 1d4',
            'mace 1d6',
            'sling 1d4',
            'war hammer 1d6',
            'staff 1d4'
            ])
            self.inventory.append(weapon)
            if weapon not in two_handed_weapons and weapon != 'sling 1d4': self.inventory.append('shield AC +1')

        if self.job == 'Druid':
            self.hp = randint(1, 6) + self.get_conmod()
            self.death_save = 11
            self.wand_save = 12
            self.poison_save = 14
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = 'Neutral'
            self.inventory.append('leather armor AC 7 [12]')
            weapon = choice([
            'club 1d4',
            'dagger 1d4',
            'sling 1d4',
            'spear 1d6',
            'staff 1d4'
            ])
            self.inventory.append(weapon)
            if weapon not in two_handed_weapons and weapon != 'sling 1d4': self.inventory.append('shield AC +1')
            druid_spells = [
                'Animal Friendship',
                'Detect Danger',
                'Entangle',
                'Faerie Fire',
                'Invisibility to Animals',
                'Locate Plant or Animal',
                'Predict Weather',
                'Speak with Animals'
            ]
            self.spells_known.append(choice(druid_spells))

        if self.job == 'Fighter':
            self.hp = randint(1, 8) + self.get_conmod()
            self.death_save = 12
            self.wand_save = 13
            self.poison_save = 14
            self.breath_save = 15
            self.spell_save = 16
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
            self.inventory.append(choice(armor))
            weapon = choice(two_handed_weapons + one_handed_weapons)
            self.inventory.append(weapon)
            if weapon not in two_handed_weapons and weapon != 'sling 1d4': self.inventory.append('shield AC +1')

        if self.job == 'Illusionist':
            self.hp = randint(1, 4) + self.get_conmod()
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
            self.inventory.append(choice(['dagger 1d4', 'staff 1d4']))
            illusionist_spells = [
                'Auditory Illusion',
                'Chromatic Orb',
                'Colour Spray',
                'Dancing Lights',
                'Detect Illusion',
                'Glamour',
                'Hypnotism',
                'Light',
                'Phantasmal Force',
                'Read Magic',
                'Wall of Fog',
                'Spook'
            ]
            self.spells_known.append(choice(illusionist_spells))

        if self.job == 'Knight':
            self.hp = randint(1, 8) + self.get_conmod()
            self.death_save = 12
            self.wand_save = 13
            self.poison_save = 14
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
            self.inventory.append(choice(['chain armor AC 5 [14]', 'plate armor AC 3 [16]']))
            weapon = choice([
            'club 1d4',
            'dagger 1d4',
            'hand axe 1d6',
            'mace 1d6',
            'short sword 1d6',
            'silver dagger 1d4',
            'spear 1d6',
            'sword 1d8',
            'war hammer 1d6'
            'battle axe 1d8',
            'staff 1d4',
            'two-handed sword 1d10',
            'polearm 1d10',
            'lance 1d6'
            ])
            self.inventory.append(weapon)
            if weapon not in two_handed_weapons and weapon != 'sling 1d4': self.inventory.append('shield AC +1')

        if self.job == 'Magic-User':
            self.hp = randint(1, 4) + self.get_conmod()
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
            self.inventory.append(choice(['dagger 1d4', 'staff 1d4']))
            magic_user_spells = [
                'Charm Person',
                'Detect Magic',
                'Floating Disc',
                'Hold Portal',
                'Light',
                'Magic Missile',
                'Protection from Evil',
                'Read Languages',
                'Read Magic',
                'Sleep',
                'Shield',
                'Ventriloquism'
            ]
            self.spells_known.append(choice(magic_user_spells))

        if self.job == 'Paladin':
            self.hp = randint(1, 8) + self.get_conmod()
            self.death_save = 10
            self.wand_save = 11
            self.poison_save = 12
            self.breath_save = 13
            self.spell_save = 14
            self.alignment = 'Lawful'
            self.inventory.append(choice(armor))
            weapon = choice(two_handed_weapons + one_handed_weapons)
            self.inventory.append(weapon)
            if weapon not in two_handed_weapons and weapon != 'sling 1d4': self.inventory.append('shield AC +1')

        if self.job == 'Ranger':
            self.hp = randint(1, 8) + self.get_conmod()
            self.death_save = 12
            self.wand_save = 13
            self.poison_save = 14
            self.breath_save = 15
            self.spell_save = 16
            self.alignment = choice(['Lawful', 'Neutral'])
            self.inventory.append(choice(['leather armor AC 7 [12]', 'chain armor AC 5 [14]']))
            weapon = choice(two_handed_weapons + one_handed_weapons)
            self.inventory.append(weapon)
            if weapon not in two_handed_weapons and weapon != 'sling 1d4': self.inventory.append('shield AC +1')

        if self.job == 'Thief':
            self.hp = randint(1, 4) + self.get_conmod()
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
            self.inventory.append('leather armor AC 7 [12]')
            weapon = choice(two_handed_weapons + one_handed_weapons)
            self.inventory.append(weapon)
        
        #hp check
        if self.hp < 1: self.hp = 1

        #figure out armor class
        self.descending_armor_class = 9
        self.ascending_armor_class = 10
        if 'leather armor AC 7 [12]' in self.inventory:
            self.descending_armor_class = 7
            self.ascending_armor_class = 12
        if 'chain armor AC 5 [14]' in self.inventory:
            self.descending_armor_class = 5
            self.ascending_armor_class = 14
        if 'plate armor AC 3 [16]' in self.inventory:
            self.descending_armor_class = 3
            self.ascending_armor_class = 16
        if 'shield AC +1' in self.inventory:
            self.descending_armor_class -= 1
            self.ascending_armor_class += 1

    def get_conmod(self):
        if self.constitution == 3: conmod = -3
        if self.constitution >= 4: conmod = -2
        if self.constitution >= 6: conmod = -1
        if self.constitution >= 9: conmod = 0
        if self.constitution >= 13: conmod = 1
        if self.constitution >= 16: conmod = 2
        if self.constitution == 18: conmod = 3
        return conmod

    def get_dexmod(self):
        if self.dexterity == 3: dexmod = -3
        if self.dexterity >= 4: dexmod = -2
        if self.dexterity >= 6: dexmod = -1
        if self.dexterity >= 9: dexmod = 0
        if self.dexterity >= 13: dexmod = 1
        if self.dexterity >= 16: dexmod = 2
        if self.dexterity == 18: dexmod = 3
        return dexmod

    def get_sheet(self):
        inventory = ', '.join(self.inventory)
        if len(self.spells_known) > 0:
            spell_list = ', '.join(self.spells_known)
            spells = f"Spells: {spell_list}"
            return f"Level 1 {self.alignment} {self.race} {self.job}\n{self.hp} HP\nAC {self.descending_armor_class - self.get_dexmod()} [{self.ascending_armor_class + self.get_dexmod()}]\nTHAC0 19 (+0)\nSTR {self.strength} INT {self.intelligence} WIS {self.wisdom} DEX {self.dexterity} CON {self.constitution} CHA {self.charisma}\nD{self.death_save} W{self.wand_save} P{self.poison_save} B{self.breath_save} S{self.spell_save}\nEquipment: {inventory}\n{spells}"
        else:
            return f"Level 1 {self.alignment} {self.race} {self.job}\n{self.hp} HP\nAC {self.descending_armor_class - self.get_dexmod()} [{self.ascending_armor_class + self.get_dexmod()}]\nTHAC0 19 (+0)\nSTR {self.strength} INT {self.intelligence} WIS {self.wisdom} DEX {self.dexterity} CON {self.constitution} CHA {self.charisma}\nD{self.death_save} W{self.wand_save} P{self.poison_save} B{self.breath_save} S{self.spell_save}\nEquipment: {inventory}"

try:
    quota = int(input("How many retainers to generate? Enter to exit.\n"))
    print('')
except:
    raise SystemExit

file = open('retainers.txt', 'a')

for x in range(quota):
    retainer = Retainer()
    print(retainer.get_sheet() + '\n')
    file.write(retainer.get_sheet() + '\n\n')

file.close()
input('Retainers exported to "retainers.txt". Press Enter to exit.')
