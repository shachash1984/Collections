"""
user_input = None
while user_input != 'done':
    user_input = input("enter a value: ")
    if user_input == 'break':
        break
    elif user_input == 'continue':
        continue
    elif user_input == 'pass':
        pass
    else:
        print (user_input)
    print("finished loop")
else:
    print("else to while")

"""
"""
test_dict = {'a':'123', 'b':'456'}
for entry in test_dict.items():
    key = entry[0]
    value = entry[1]
    print(entry, key, value)

"""

"""
test_set = {7, 8, 9, 1, 2, 3}
for i, c in enumerate(test_set):
    print(i, c)
"""
"""
r = range(-5,5,2)
print(list(r), type(r))

for i in range(0,10):
    print(i)
"""

"""

"""
def print_even(num_list):
    for i in num_list:
        if i % 2 == 0:
            print(i)
        else:
            continue

print_even(range(0,100))
