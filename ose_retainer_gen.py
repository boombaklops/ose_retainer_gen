#made by boombaklops. modify as you please, but gimme credit :)
from random import randint, choice

def generate_equipment(job):
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
        'leather armor AC 12',
        'chain armor AC 14',
        'plate armor AC 16'
    ]

    inventory = []
    if job == 'Acrobat':
        inventory.append('leather armor AC 12')
        inventory.append(choice([
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
    if job == 'Assassin':
        inventory.append('leather armor AC 12')
        weapon = choice(two_handed_weapons + one_handed_weapons)
        inventory.append(weapon)
        if weapon not in two_handed_weapons and weapon != 'sling 1d4': inventory.append('shield AC +1')
    if job == 'Barbarian' or job == 'Ranger':
        inventory.append(choice(['leather armor AC 12', 'chain armor AC 14']))
        weapon = choice(two_handed_weapons + one_handed_weapons)
        inventory.append(weapon)
        if weapon not in two_handed_weapons and weapon != 'sling 1d4': inventory.append('shield AC +1')
    if job == 'Bard':
        inventory.append(choice(['leather armor AC 12', 'chain armor AC 14']))
        weapon = choice(['short bow 1d6', 'long bow 1d6', 'crossbow 1d6'] + one_handed_weapons)
        inventory.append(weapon)
    if job == 'Cleric':
        inventory.append(choice(armor))
        weapon = choice([
        'club 1d4',
        'mace 1d6',
        'sling 1d4',
        'war hammer 1d6',
        'staff 1d4'
        ])
        inventory.append(weapon)
        if weapon not in two_handed_weapons and weapon != 'sling 1d4': inventory.append('shield AC +1')
    if job == 'Druid':
        inventory.append('leather armor AC 12')
        weapon = choice([
        'club 1d4',
        'dagger 1d4',
        'sling 1d4',
        'spear 1d6',
        'staff 1d4'
        ])
        inventory.append(weapon)
        if weapon not in two_handed_weapons and weapon != 'sling 1d4': inventory.append('shield AC +1')
    if job == 'Fighter' or job == 'Paladin':
        inventory.append(choice(armor))
        weapon = choice(two_handed_weapons + one_handed_weapons)
        inventory.append(weapon)
        if weapon not in two_handed_weapons and weapon != 'sling 1d4': inventory.append('shield AC +1')
    if job == 'Illusionist' or job == 'Magic-User':
        inventory.append(choice(['dagger 1d4', 'staff 1d4']))
    if job == 'Knight':
        inventory.append(choice(['chain armor AC 14', 'plate armor AC 16']))
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
        inventory.append(weapon)
        if weapon not in two_handed_weapons and weapon != 'sling 1d4': inventory.append('shield AC +1')
    if job == 'Thief':
        inventory.append('leather armor AC 12')
        weapon = choice(two_handed_weapons + one_handed_weapons)
        inventory.append(weapon)

    return inventory

class Retainer():

    def __init__(self):
        #stats
        self.strength = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.intelligence = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.wisdom = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.dexterity = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.constitution = randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.charisma = randint(1, 6) + randint(1, 6) + randint(1, 6)

        #race and class selection
        races = [
            'Half-Orc',
            'Human'
        ]
        jobs = [
            'Fighter',
            'Thief'
        ]
        #eligibility checks
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
        if self.job == 'Acrobat':
            self.hp = randint(1, 4)
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
        if self.job == 'Assassin':
            self.hp = randint(1, 4)
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Neutral', 'Chaotic'])
        if self.job == 'Barbarian':
            self.hp = randint(1, 8)
            self.death_save = 10
            self.wand_save = 13
            self.poison_save = 12
            self.breath_save = 15
            self.spell_save = 16
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
        if self.job == 'Bard':
            self.hp = randint(1, 6)
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
        if self.job == 'Cleric':
            self.hp = randint(1, 6)
            self.death_save = 11
            self.wand_save = 12
            self.poison_save = 14
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
        if self.job == 'Druid':
            self.hp = randint(1, 6)
            self.death_save = 11
            self.wand_save = 12
            self.poison_save = 14
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = 'Neutral'
        if self.job == 'Fighter':
            self.hp = randint(1, 8)
            self.death_save = 12
            self.wand_save = 13
            self.poison_save = 14
            self.breath_save = 15
            self.spell_save = 16
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
        if self.job == 'Illusionist':
            self.hp = randint(1, 4)
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
        if self.job == 'Knight':
            self.hp = randint(1, 8)
            self.death_save = 12
            self.wand_save = 13
            self.poison_save = 14
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
        if self.job == 'Magic-User':
            self.hp = randint(1, 4)
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])
        if self.job == 'Paladin':
            self.hp = randint(1, 8)
            self.death_save = 10
            self.wand_save = 11
            self.poison_save = 12
            self.breath_save = 13
            self.spell_save = 14
            self.alignment = 'Lawful'
        if self.job == 'Ranger':
            self.hp = randint(1, 8)
            self.death_save = 12
            self.wand_save = 13
            self.poison_save = 14
            self.breath_save = 15
            self.spell_save = 16
            self.alignment = choice(['Lawful', 'Neutral'])
        if self.job == 'Thief':
            self.hp = randint(1, 4)
            self.death_save = 13
            self.wand_save = 14
            self.poison_save = 13
            self.breath_save = 16
            self.spell_save = 15
            self.alignment = choice(['Lawful', 'Neutral', 'Chaotic'])

        #equipment
        self.inventory = generate_equipment(self.job)

    def get_sheet(self):
        #figure out armor class
        armor_class = 10
        if 'leather armor AC 12' in self.inventory:
            armor_class = 12
        if 'chain armor AC 14' in self.inventory:
            armor_class = 14
        if 'leather armor AC 16' in self.inventory:
            armor_class = 16
        if 'shield AC +1' in self.inventory:
            armor_class += 1
        inventory = '\n'.join(self.inventory)
        return f"Level 1 {self.alignment} {self.race} {self.job}\n{self.hp} HP\nAC {armor_class}\nTHAC0 19 (+0)\nSTR {self.strength} INT {self.intelligence} WIS {self.wisdom} DEX {self.dexterity} CON {self.constitution} CHA {self.charisma}\nD {self.death_save} W {self.wand_save} P {self.poison_save} B {self.breath_save} S {self.spell_save}\nEquipment:\n{inventory}\n\n"

try:
    quota = int(input("How many retainers to generate? Enter to exit.\n"))
    print('')
except:
    raise SystemExit

file = open('retainers.txt', 'a')

for x in range(quota):
    retainer = Retainer()
    print(retainer.get_sheet())
    file.write(retainer.get_sheet())

file.close()
print('Retainers exported to "retainers.txt".')