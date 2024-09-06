Here's the solution to the problem of making a palindrome of a given string:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.

    if not string: 
        return ""
    if len(string) == 1: 
        return string

    longest_palindrome = ""
    for char in string:
        if is_palindrome(char):
            longest_palindrome = char + longest_palindrome[::-1]
        else: 
            break

    return longest_palindrome
```
This code defines two functions: is_palindrome checks if a given string is a palindrome, and make_palindrome creates a palindrome from a given string.

The code efficiently finds the longest palindrome by iterating through each character and checking if it's a palindrome. If the character is a palindrome, it appends it to the beginning of the longest palindrome. If the character is not a palindrome, it stops the appending process.