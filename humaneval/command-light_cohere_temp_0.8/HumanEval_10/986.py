```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    elif string == "":
        return ""
    else:
        l = len(string)
        reverse = string[::-1]
        postfix = ""
        for i in range(0, l):
            if is_palindrome(reverse + string[i]):
                postfix += string[i]
                break
            else:
                postfix += string[i].swap()
        return postfix + reverse
```
The function make_palindrome generates the shortest palindrome using a simple algorithm. It first checks if the recommended using a pre-existing palindrome as a prefix. The function returns if the strings are empty, otherwise, it uses a for loop to find the longest palindrome. Then, it appends the string with the first part of the reverse of the palindrome found, until the current character is not a palindrome itself. 

This function effectively generates a palindrome from the input string.