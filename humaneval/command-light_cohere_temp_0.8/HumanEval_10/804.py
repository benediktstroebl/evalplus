The solution is a Palindrome Generator Function in Python.

The approach is to first find the longest palindrome prefix in the string, and then append the reverse of that prefix to the string.

Here's the code:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    
    char = string[0]
    new_string = char
    is_palindrome = True
    for char in string[1:]:
        if not is_palindrome:
            break
        new_string = new_string + char
        is_palindrome = is_palindrome and char == new_string[::-1]
    return new_string
```
The function is_palindrome returns True if the string is a palindrome, and False otherwise.