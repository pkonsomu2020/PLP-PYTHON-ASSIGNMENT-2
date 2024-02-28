# Creating an empty list called my_list
my_list = []

# Appending the elements to the list
my_list.extend([10, 20, 30, 40])

# Inserting value 15 at the second position of the list
my_list.insert(1, 15)

# Extend my_list with another list
my_list.extend([50, 60, 70])

# Removing the last element in the my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("Index of 30 in my_list:", index_30)

# Print my_list
print("my_list after all operations:", my_list)