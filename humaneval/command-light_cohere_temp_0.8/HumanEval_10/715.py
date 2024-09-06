This Python script contains a self-contained solution to the problem of creating the longest palindrome from a given string.

```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""

    palindrome = []
    reverse_string = string[::-1]
    while True:
        if reverse_string[-1:] not_palindrome[-1] == True:
            # If the last character matches the prefix, append it to the current palindrome
            palindrome.append(reverse_string[1:])
            reverse_string = reverse_string[:-0]
        else:
            # Otherwise, append the character to the current palindrome
            palindrome.append(reverse_string[1])
            reverse_string = reverse_string[:-0]

    return ''.join(palindrome)
```