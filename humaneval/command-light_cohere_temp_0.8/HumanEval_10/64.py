```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Algorithm idea: simple palindrome generator using prefix and suffix
    pal = []
    reversed_pal = []
    
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            pal.append(string[i])
            reversed_pal.append(string[::-1][i -len(string[::-1])])
        else:
            pal.append(string[i])
            reversed_pal.append(string[::-1][i -len(string[::-1])])
            break
    
    palindrome = ''.join(reversed(pal))
    return palindrome
```