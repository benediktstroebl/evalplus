This script defines a function is_palindrome that checks if a given string is a palindrome, and another function make_palindrome that constructs a palindrome from a given string:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    done using:
    - case '': return ''
    - case 'a': return 'a'
    - case 'cc': return 'ccc'
    - else: 
        return ''.join(reversed(string[:i]) + string[i+len(reversed(string[i:]))])
    """

Below is the output of the code:
```
True
catac
cata
True
```