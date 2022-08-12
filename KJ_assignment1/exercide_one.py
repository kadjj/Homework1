"""
1) Write a program to create a new string made of the middle three characters of an input string.
"""

input = 'JhonDipPeta'
#result = Dip
print("1) " + str(input[4:7]))

"""
2) Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
"""
s1 = "Aunt"
s2 = "Sister"
# s3 = s1.insert[1, s2])
middle = int(len(s2) / 2)
x = s2[:middle:]
x = x + s1
s3 = x + s2[middle:]
print("2) " + str(s3))

