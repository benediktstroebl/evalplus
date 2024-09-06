Here's a self-contained Python function that checks if a given string is a palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    lps = []
    for i, char in enumerate(string):
        if char == string[i - 1] and i > 0:
            lps.append(char)

    # Reverse thelps then construct the reverse of a palindrome
    return ''.join(''.join(lps[::-1], string))
```