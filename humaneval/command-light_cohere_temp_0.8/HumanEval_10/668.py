Here is a Python script with a self-contained function that solves the problem of finding the shortest palindrome that begins with a supplied string:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    if not is_palindrome(string):
        return ''  # Returns empty string if not palindrome
    palindrome = []
    while True:
        # Add first character to palindrome
        palindrome.append(string[0])
        
        # Find a palindrome by removing first and last characters, then reverse and check if the middle is also a palindrome.
        has_palindrome = False
        for i in range(1,len(string)):
            if string[i] == string[i-1]:
                has_palindrome = True
                break
        
        if has_palindrome:
            break

        # Append rest of the string to palindrome
        palindrome.extend(string[i:])
    return ''.join(palindrome)
```
This script defines a function is_palindrome that checks if a given string is a palindrome and another function make_palindrome that uses this is_palindrome function to find the shortest palindrome.