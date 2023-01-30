# 3rd quest = Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.



# Sample String : 'The quick Brow Fox'

# Expected Output :

# No. of Upper case characters : 3

# No. of Lower case Characters : 12


def stringcase():
    string = input("Enter a string: ")
    upper_case_count = 0
    lower_case_count = 0

    for i in string:
        if i.islower():
            lower_case_count += 1
        else:
            if  i.isupper():
                upper_case_count +=1
        

    print("Total Upper case letters: ", upper_case_count)
    print("Total lower case letters: ", lower_case_count)

stringcase()