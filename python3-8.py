# 3-1
years_list = [1993, 1994, 1995, 1996, 1997, 1998]

print(years_list)

# 3-2
print(years_list[2])

# 3-3
print(years_list[-1])

# 3-4
things = ["mozzarella", "cinderella", "salmonella"]

# 3-5
things[1] = things[1].capitalize()
print(things)

# 3-6
things[0] = things[0].upper()
print(things)

# 3-7
del things[-1]
print(things)

# 3-8
surprise = ["Groucho", "Chico", "Harpo"]

# 3-9
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1].capitalize()

print(surprise)

# 3-10
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

# 3-11
print(e2f['walrus'])

# 3-12
f2e = {}
for english, french in e2f.items():
    f2e[french] = english

print(f2e)

# 3-13
print(f2e['chien'])

# 3-14
print(set(e2f.keys()))

# 3-15
life = {
    'animals': {
        'cats': [
            'Henry',
            'Grumpy',
            'Lucy',
        ],
        'octopi': {},
        'emus': {},
    },
    'plants': {},
    'other': {}
}
print(life)

# 3-16
print(life.keys())

# 3-17
print(life['animals'].keys())

# 3-18
print(life['animals']['cats'])
