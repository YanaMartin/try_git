

colours = {
    'pear': 'green',
    'apple': 'red',
    'melon': 'green',
    'plum': 'purple',
    'radish': 'red',
    'cabbage': 'green',
    'carrot': 'orange',
}
colour_riped = dict(colours)
for key in colour_riped:
    colour_riped[key] = 'blackish-brownish-' + colour_riped[key]
print(colours['apple'])
print(colour_riped)

#why empty?
