Here is a Python script that contains a self-contained function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    palindrome = []
    l = 0
    while True:
        if l == len(string) or is_palindrome(string[l:]):
            palindrome.append(string[l:])
        l += 1
    reverse_prefix = string[::-1][:l]
    palindrome.append(reverse_prefix)

    return ''.join(palindrome)
```
This script defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` creates a palindrome from a given string. The `make_palindrome` function uses a simple algorithm to find the shortest palindrome. It iterates over theread the pattern of appending the first prefix of the string that is also a palindrome, and the reverse of the prefix at each iteration until it encounters the end of the string or the prefix of a palindrome.