color = ['red', 'green', 'yellow', 'pink', 'blue']
print(color)

color[0] = 'black'
print(color)

print("\n> Adding element in list :")
color = ['red', 'green', 'yellow', 'pink', 'blue']
color.append('orange')
print(color)
print("\n--------------------------------------------------------------")
print("\n> Inserting element into a list :")
color = ['red', 'green', 'yellow', 'pink', 'blue']
color.insert(1, 'black')
print(color)
print("\n--------------------------------------------------------------")
print("\n> Delete element from list :")
color = ['red', 'green', 'yellow', 'pink', 'blue']
del color[0]
print(color)
print("\n--------------------------------------------------------------")
print("\n> Removing iteam using pop :")
print("Note : \nThe pop() method removes the last item in a list, but it lets you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list.")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("\n--------------------------------------------------------------")
print("\n> Popping items from any position in a list :")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print("\n--------------------------------------------------------------")
print("\n> Removing an item by value :")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
