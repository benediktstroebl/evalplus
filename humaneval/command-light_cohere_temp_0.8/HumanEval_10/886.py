Here is a self-contained Python function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """ Returns string = ''.join(string)
    while True: 
        char = string[0]
        if char == char[::-1]: 
            # Found a palindrome, break the loop
            break
        string = char + string[1:]
    return string
```

This function takes a string as input and returns a palindrome of the original string. The algorithm idea is to find the longest palindrome using the prefix-matching technique, which helps avoid unnecessary characters and makes the code more concise.