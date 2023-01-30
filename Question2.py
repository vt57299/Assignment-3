#  2. Write a Python program to reverse a string.



# Sample String : "1234abcd"

# Expected Output : "dcba4321"

# Solution:


def revstr():
    string = input("Enter a string: ")
#     rev_string = string[::-1]
#     return rev_string

    rev_string = ""
    for i in string:
        rev_string = i + rev_string
    return rev_string

output = revstr()
print("Reversed string: ", output)