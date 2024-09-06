Below is a Python script with a self-contained function that creates the longest palindrome from a given string:

```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.

    if not string:
        return ''

    palindrome = ''
    left, right = 0, len(string) - 1

    while left <= right:
        if is_palindrome(string[left:right + 1]):
            palindrome += string[left:right + 1][::-1]
            left += 1
        else:
            right -= 1

    return palindrome
```