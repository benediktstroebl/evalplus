Here's a Python script with a self-contained function that solves the problem of forming the shortest palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic postfix.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[i:]):
        i -= 1

    # Find the longest string prefix that comes before the palindromic suffix.
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1

    return make_palindrome(string[:j] + string[i:j][::-1] + string[j:])
```

This algorithm starts by checking if the original string is a palindrome and uses that if it is. It otherwise finds the longest substring that forms a palindrome and iterates backwards from there. It then finds the largest prefix of the string that comes before this palindrome and reverses that to join it with the palindrome. It does this while making sure not to go out of bounds during the process.