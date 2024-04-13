name = ["adan","josue","jeronimo"]
message = f'Hello {name[0].title()}!'
print(message)

name[1] = 'middle name'
print(name)

name.append('hernandez')
print(name)

name.insert(1, "josue")
print(name)

del name[2]
print(name)

name.remove('hernandez')
print(name)

lastname = name.pop()
hehe = f'her future last name will be {lastname}'
print(hehe)