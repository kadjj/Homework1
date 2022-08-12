"""
1) Reverse a given list in python
"""

info = ['karl', 100, 'Red', 'mangoes']
info.reverse()
print("1) Reversed list is: " + str(info))

"""
2)Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
Hint: use list comprehension with zip function
"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
final_list = list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3]
print("2.1) Final list is: " + str(final_list))

final_list2 = [i+j for (i,j) in zip(list1, list2)]
print("2.2) Final list is: " + str(final_list2))

"""
3)Write a Python program to find the second largest number in the given list.
"""
list1 = [10, 20, 4]
list1.sort()
print("3.1)Second largest number in the list is: " + str(list1[-2]))

list2 = [70, 11, 20, 4, 100]
list2.sort()
list2.reverse()
print("3.2)Second largest number in the list is: " + str(list2[1]))

"""
4) Concatenate two list
Hint: use list comprehension
<<new_list>> = [expression for item in list1 for y in list2]
"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = [j for i in [list1, list2] for j in i]
print ("4) Concatenated list: "+ str(res))

"""
5) Write a program to find value 20 in the list, 
and if it is present, replace it with 200. Only update the first occurrence of an item.
"""
a_list = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(a_list)):
    if a_list[i] == 20:
        a_list[i] = 200 # I don't know how to update only the first 20
print("5) Replaced list is: " + str(a_list))

"""
6)count number of occurrences of x in the given list
"""
Input : list = [15, 6, 7, 10, 12, 20, 10, 28, 10]





"""
7) write a program to remove all occurrences of item 20
Hint: list comprehension
"""
list1 = [5, 20, 15, 20, 25, 50, 20]
newlist = [x for x in list1 if x != 20]

print("7) New list without 20 is: " + str(newlist))

"""
8)Write a program to return the middle value of a list. If there are 2 middle values, return the second
"""

