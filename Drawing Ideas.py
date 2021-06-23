import random
height=['tall', 'short', 'midsized']
weight=['skinny', 'fat', 'muscly', 'lean']
gender=['female', 'male', 'non-binary', 'genderfluid', 'androgynous']
race=['dwarf', 'elf', 'gnome', 'half-elf', 'halfling', 'half-orc', 'human', 'tiefling', 'orc', 'satyr', 'goliath', 'goblin', 'fairy', 'firbolg']
class1=['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard', 'artificer']
hlength=['very long', 'long', 'mid-length', 'short', 'very short']
hcolor=['blonde', 'brown', 'black', 'white', 'gray', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'multicolored']
ecolor=['brown', 'green', 'blue', 'black', 'hazel', 'white', 'red', 'pink', 'purple', 'yellow', 'gray', 'orange', 'multicolored']

sentence ='A '+random.choice(height)+', '+random.choice(weight)+', '+random.choice(gender)+' '+random.choice(race)+' '+random.choice(class1)+', with '+random.choice(hlength)+' '+random.choice(hcolor)+' hair, and '+random.choice(ecolor)+' eyes.'

import random
size=['tiny', 'small', 'medium', 'large', 'huge', 'gargantuan']
alignment1=['chaotic', 'neutral', 'lawful']
alignment2=['good', 'neutral', 'evil']
type=['aberration', 'beast', 'celestial', 'construct', 'dragon','elemental', 'fey', 'fiend', 'giant','humanoid', 'monstrosity', 'ooze', 'plant', 'undead']
environment=['anywhere', 'in the hills', 'in the mountains', 'in the ocean', 'in the forest', 'in the desert', 'underground', 'in another plane', 'in volcanoes', 'in the snow', 'in a jungle', 'in a swamp', 'in trash', 'amongst people']
color=['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white', 'brown', 'golden', 'silver', 'gray', 'pink']

sentence2 ='A '+random.choice(size)+', '+random.choice(color)+', '+random.choice(alignment1)+' '+random.choice(alignment2)+' '+random.choice(type)+', that lives '+random.choice(environment)+'.'

import random
mapsize=['An extra small', 'A small', 'A medium', 'A large', 'An extra large']
maptype=['a castle', 'a dungeon', 'a house', 'some ruins', 'a forest', 'a mansion', 'a labyrinth', 'a ship', 'a town', 'an island', 'a city']

sentence3 =random.choice(mapsize)+' map of '+random.choice(maptype)+'.'

import random
horoscope=['Aries', 'Taurus', 'Leo', 'Scorpio', 'Libra', 'Virgo', 'Capricorn', 'Aquarius', 'Pisces', 'Gemini', 'Cancer', 'Sagittarius']
weapon=['Knife', 'Scimitar', 'Sword', 'Short Sword', 'Hammer', 'Axe', 'Pickaxe', 'Whip', 'Club', 'Dagger', 'Mace', 'Sickle', 'Spear', 'Quarterstaff', 'Crossbow', 'Bow', 'Blowgun', 'Slingshot', 'Trident', 'Net', 'Claws', 'Fangs', 'Poison', 'Venom', 'Electricity', 'Fire', 'Ice']
maincolor=['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Black', 'Brown', 'White', 'Silver', 'Gray', 'Golden', 'Pink']
palette=['Monochromatic', 'Analogous', 'Complimentary', 'Triadic Complimentary', 'Split Complimentary', 'Tetradic']

sentence4 ='Horoscope: '+random.choice(horoscope)+"""
Weapon of Choice: """+random.choice(weapon)+"""
Main Color: """+random.choice(maincolor)+"""
Color Palette: """+random.choice(palette)

while True:
    s = input('''
What would you like to draw? ''')
    if s == "nothing":
        break
    if s == "a person":
        while True:
            sentence ='A '+random.choice(height)+', '+random.choice(weight)+', '+random.choice(gender)+' '+random.choice(race)+' '+random.choice(class1)+', with '+random.choice(hlength)+' '+random.choice(hcolor)+' hair, and '+random.choice(ecolor)+' eyes.'
            print(sentence)
            a = input('''
What about this?''')
            if a == "no":
                continue
            if a == "yes":
                print("""
Have fun drawing!
Done""")
                quit()
            if a == "start over":
                break
    if s == "a monster":
        while True:
            sentence2 ='A '+random.choice(size)+', '+random.choice(color)+', '+random.choice(alignment1)+' '+random.choice(alignment2)+' '+random.choice(type)+', that lives '+random.choice(environment)+'.'
            print(sentence2)
            a = input('''
What about this?''')
            if a == "no":
                continue
            if a == "yes":
                print("""
Have fun drawing!
Done""")
                quit()
            if a == "start over":
                break
    if s == "a map":
        while True:
            sentence3 =random.choice(mapsize)+' map of '+random.choice(maptype)+'.'
            print(sentence3)
            a = input('''
What about this?''')
            if a == "no":
                continue
            if a == "yes":
                print("""
Have fun drawing!
Done""")
                quit()
            if a == "start over":
                break
    if s == "i just need some inspiration":
        while True:
            sentence4 ='Horoscope: '+random.choice(horoscope)+"""
Weapon of Choice: """+random.choice(weapon)+"""
Main Color: """+random.choice(maincolor)+"""
Color Palette: """+random.choice(palette)
            print(sentence4)
            a = input('''
What about this?''')
            if a == "no":
                continue
            if a == "yes":
                print("""
Have fun drawing!
Done""")
                quit()
            if a == "start over":
                break

print("Done.")
