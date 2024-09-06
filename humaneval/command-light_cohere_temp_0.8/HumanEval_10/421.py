Here is a Python script that demonstrates the solution to the problem of finding the shortest palindrome using a recursive approach:

```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    if is_palindrome(string[:-len(string) // 2]):
        return string
    return make_palindrome(string[::len(string) // 2:]) + string[:len(string) // 2]
```

This function follows a recursive approach to find the shortest palindrome using the `is_palindrome` helper function. The base case returns an empty string, and in the recursive call, the function finds the palindrome by checking the prefix of the string against the reversed string, and then constructs the palindrome by appending the reversed prefix to the reversed suffix.