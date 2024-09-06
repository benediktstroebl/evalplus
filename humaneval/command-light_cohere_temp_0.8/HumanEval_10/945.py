Here's the provided Python code that includes a self-contained function to create the palindrome of a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    
    if not string:
        return ''
    
    # Find the longest postfix of supplied string that is a palindrome
    longest_palindrome = []
    for char in string:
        if char == char[::-1]:
            longest_palindrome.append(char)
   
    return longest_palindrome
```

The function `make_palindrome` takes a string as input and uses the `is_palindrome` function to check if each character in the string is its own reverse, and if it is, it appends it to the `longest_palindrome` list.