#arrays
colleagues = ["Jim", "Jim", "Jim", "Lara", "Jay", "Dennis", "Megan", "Jillian", "Jenn", "Ian"]
colleagues[1] = "Mewko"
lucky_numbers = [4, 8, 12, 16, 99, 45, 72]

# add to the end of the array
# colleagues.extend(lucky_numbers)

# insert into the array
# colleagues.insert(3, "Dink")

# remove the whole list
# colleagues.clear()

# remove the last element
colleagues.pop()

# where in the array is the thing
# print(colleagues.index("Dink"))
# print(colleagues.index(3)) <-- not in the list!!!

# count how many of the item
# here we'll only get 2 because mewko is causing more trouble
# print(colleagues.count("Jim"))

# ascending the array, with numbers it will start from the lowest and work up
# colleagues.sort()

# descending the array
# colleagues.reverse()

# copy the array
colleagues2 = colleagues.copy()

print(colleagues2)