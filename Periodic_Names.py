elements_dict={'u': 'Uranium', 'cl': 'Chlorine', 'ga': 'Gallium', 'ta': 'Tantalum', 'tc': 'Technetium', 'fr': 'Francium', 'in': 'Indium', 'sm': 'Samarium', 'zn': 'Zinc', 'li': 'Lithium', 'ts': 'Tennessine', 'ag': 'Silver', 'pu': 'Plutonium', 'rn': 'Radon', 'cf': 'Californium', 'ca': 'Calcium', 'ti': 'Titanium', 'ra': 'Radium', 'mg': 'Magnesium', 'at': 'Astatine', 'rh': 'Rhodium', 'rg': 'Roentgenium', 'pd': 'Palladium', 'np': 'Neptunium', 'dy': 'Dysprosium', 'ho': 'Holmium', 'mc': 'Moscovium', 'ac': 'Actinium', 'lv': 'Livermorium', 'hf': 'Hafnium', 'gd': 'Gadolinium', 'ir': 'Iridium', 'tl': 'Thallium', 'ni': 'Nickel', 'y': 'Yttrium', 'lr': 'Lawrencium', 'cr': 'Chromium', 'sb': 'Antimony', 'ge': 'Germanium', 'ce': 'Cerium', 'as': 'Arsenic', 'ds': 'Darmstadtium', 'no': 'Nobelium', 'tb': 'Terbium', 'zr': 'Zirconium', 'hs': 'Hassium', 'es': 'Einsteinium', 'nh': 'Nihonium', 'cs': 'Cesium', 'kr': 'Krypton', 'i': 'Iodine', 'os': 'Osmium', 'fl': 'Flerovium', 'pb': 'Lead', 'au': 'Gold', 'sn': 'Tin', 'eu': 'Europium', 'w': 'Tungsten', 'er': 'Erbium', 'la': 'Lanthanum', 'rf': 'Rutherfordium', 'se': 'Selenium', 'cu': 'Copper', 'cm': 'Curium', 'mt': 'Meitnerium', 'tm': 'Thulium', 'b': 'Boron', 'o': 'Oxygen', 'mo': 'Molybdenum', 'sc': 'Scandium', 'f': 'Fluorine', 'v': 'Vanadium', 'pa': 'Protactinium', 'md': 'Mendelevium', 'he': 'Helium', 're': 'Rhenium', 'te': 'Tellurium', 'th': 'Thorium', 'k': 'Potassium', 'ba': 'Barium', 'lu': 'Lutetium', 'nb': 'Niobium', 'sr': 'Strontium', 'br': 'Bromine', 'na': 'Sodium', 'po': 'Polonium', 'og': 'Oganesson', 'n': 'Nitrogen', 'si': 'Silicon', 'db': 'Dubnium', 'be': 'Beryllium', 'al': 'Aluminum, Aluminium', 'ar': 'Argon', 'c': 'Carbon', 'pr': 'Praseodymium', 's': 'Sulfur', 'mn': 'Manganese', 'hg': 'Mercury', 'am': 'Americium', 'pt': 'Platinum', 'p': 'Phosphorus', 'co': 'Cobalt', 'cn': 'Copernicium', 'h': 'Hydrogen', 'fm': 'Fermium', 'ne': 'Neon', 'yb': 'Ytterbium', 'rb': 'Rubidium', 'xe': 'Xenon', 'nd': 'Neodymium', 'cd': 'Cadmium', 'fe': 'Iron', 'pm': 'Promethium', 'sg': 'Seaborgium', 'ru': 'Ruthenium', 'bk': 'Berkelium', 'bh': 'Bohrium', 'bi': 'Bismuth'}

def main_func():
    print("Can I get a name to process?")
    name = input()
    name_lowercase = name.lower()
    print("\nAnd the elements in your name are-")
    for symbol in elements_dict:
        if symbol in name_lowercase:
            print(symbol.title(), "-", elements_dict[symbol])
    print("\nDo you want to try again? Yes/No")
    choice=input()
    if choice.lower()=="yes":
        main_func()
    else:
        exit()

main_func()

