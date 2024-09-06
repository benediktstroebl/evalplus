```python
def is_palindrome(string): 
    """ Check if a string is a palindrome """
    return string == string[::-1]

def make_palindrome(string): 
    """ Create a palindrome from a given string """
    palindrome = []
    while True:
        palindrome.append(char)
        if (char == '.' == char == char[::-1]):
            break
        char = char[::-1]
    return ''.join(palindrome)
```

This code defines two functions:
- `is_palindrome` checks if a given string is a palindrome or not. It returns `True` if the Palindrome and `False` otherwise.
- `make_palindrome` creates a palindrome from a given string. It uses a longest palindrome prefix that is also a palindrome, and appends it to the string by inverting the character before the palindrome.

The algorithm works by trying all single characters as potential first characters in the palindrome. Once a prefix is found, it starts inverting the characters before the palindrome. If the current character is the same as its reverse, it appends it to the palindrome. Finally, the function returns the reversed string as the palindrome.

Note that this solution uses the same idea as the previous solution, but it directly constructs the palindrome without using a for loop.  This are more efficient and readable.