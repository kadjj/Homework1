"""
1) Reverse the order of words in a given sentence.
"""
str_val = "Hello World"
s = str_val.split()[::-1]
l = []
for i in s:
    # appending reversed words to l
    l.append(i)
# printing reverse words
print("1) " + " ".join(l))

"""2) write a program  that takes a list and returns 
a new list that contains all the elements of the 
first list minus all the duplicates."""
list1 = {10, 23, 23, 5, 67, 10}
# set removes duplicates { }
print("2) New list is : " + str(list1))

"""3)Write a password strength verifier in Python that checks if user password is strong.
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
"""
password1 = input("Write your password: ")

import string
a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = string.punctuation
f = [a, b, c, d]
sum1 = 0
for x in f:
    sum1 += (set(password1) & set(x)) != set()
print("3) "+ str('True' if sum1 == 4 else 'False'))


"""4) Write a program to reverse row sort in list of lists
"""
list_id = [[4,1,6], [7,9], [8,9,2,4]]
result = [[6,4,1], [9,7], [9,8,4,2]]

print("4.1) The original list is : " + str(list_id))

# Reverse Row sort in Lists of List using loop
for ele in list_id:
    ele.sort(reverse=True)
print("4.2) The reverse sorted Matrix is : " + str(list_id))

"""5) Write a program to pair elements with rear element in matrix row 
"""
list1 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
print("5.1) original list: " + str(list1))

# Pair elements with Rear element in Matrix Row using list comprehension
res = []
for sub in list1:
    res.append([[ele, sub[-1]] for ele in sub[:-1]])
print("5.2) The list after pairing elements: " + str(res))

"""6) Replace each special symbol with # in the following string
Hint: import string, and use string.punctuation
"""
str1 = "%There &are three( students$ and& 1 trainer!"

print("6)I don't know how to do this program")


"""7) Remove all characters for string except integers
hint: list comprehension and isdigit()"""

str1 = "My mum has a 10 year old dog and 2 fishes"
#result = 102
res = [x for x in str1 if x.isdigit()]
res = ''.join(res)
print("7) " + str(res))


"""8)Remove all empty strings from a list of strings
"""

name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes', 'Hello Dear', '', 'Hello Sir']
cleaned = []
for x in name_list:
    if x != "":
        cleaned.append(x)
print("8) Cleaned list is :" + str(cleaned))
