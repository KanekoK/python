# 4-1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

# 4-2
guess_me = 7
start = 1
while start <= guess_me:
    if start < guess_me:
        print('too low')
    else:
        print('found it!')
    start += 1
print('oops')
# ++や--はPythonにはない

# 4-3
for word in [3, 2, 1, 0]:
    print(word)

# 4-4
even = [number for number in range(10) if number % 2 == 0]

print(even)

# 4-5
squares = {key: key*key for key in range(10)}
print(squares)

# 4-6
odd = {item for item in range(10) if item % 2 == 1}
print(odd)

# 4-7
for thing in ('Got %s' % number for number in range(10)):
    print(thing)

# 4-8
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())
# 4-9
def get_odds():
    for number in range(1, 10, 2):
        yield number
# ジェネレータ関数はreturn文ではなく、yield文で返す

for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print("The third odd number is", number)
        break

# 4-10
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
        return new_func

@test
def greeting():
    print("Greetings, Earthling")

# greeting()

# 4-11


# 4-12

