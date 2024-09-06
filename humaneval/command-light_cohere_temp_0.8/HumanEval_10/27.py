Here's a self-contained Python function that solves the problem of making a palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]
 
def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    
    # Algorithm idea simple:
    # Find the longest postfix of supplied string that is a palindrome.
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    if not string:
        return ""

    # Find the index of the longest palindromic substring
    index = 0
    palindromic_length = 1
    while True:
        index = string[index: index + palindromic_length].find('ator')
        if index == -1:
            break
        palindromic_length += 1

    # Append the reverse of the found palindrome as the suffix
    return string[:index] + string[-index:]
```
This code defines two functions: is_palindrome and make_palindrome. The is_palindrome function checks if a given string is a palindrome or not. It returns True for an input that is not a palindrome. The make_palindrome function creates a new string that contains the shortest palindrome that begins with the original string. It does this by trying to find the longest palindromic substring in the original string and then appends the reverse of this substring as the end of the new string.