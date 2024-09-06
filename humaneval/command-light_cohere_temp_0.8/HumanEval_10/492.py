Here is a self-contained Python script with a function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:  # empty string is palindrome
        return ""

    palindrome = []
    while True:
        palindrome.append(char)
        if (char == char[:-1]) or char == char[-1:]  :
            break
    return ''.join(palindrome)
```
The code defines two functions:
1. Palindrome - takes a longest palindrome substring within the input string.
2. PalindromeGen takes generate the count the number of palindromic characters, and append the character if it is a palindrome or append the previous palindrome if it is not a palindrome.