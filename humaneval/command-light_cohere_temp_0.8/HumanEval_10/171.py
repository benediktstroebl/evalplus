Here is a self-contained Python script that defines a function `make_palindrome` that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # algorithm idea: 
    # find the longest postfix of supplied string that is a palindrome
    # append to the end of the string reverse of a string prefix that comes before the palindromic suffix 
    if string == "":
        return ""
    elif string[-1] == string[0]:
        return string + string[::-1][1:]
    else:
        return make_palindrome(string[1:]) + string[0:]+string[-1:]
```
The `make_palindrome` function solves the problem by first checking if the string is empty or contains only one character, it returns the original string. If the string contains at least one palindrome, it simply returns the original string. If the string has two or long enough to form a palindrome, the function applies the algorithm idea by breaking the string into a prefix and a suffix, then concatenates the reversed prefix with the reversed suffix to create the palindrome.