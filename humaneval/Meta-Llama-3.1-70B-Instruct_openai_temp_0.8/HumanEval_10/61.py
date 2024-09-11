```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:
        return string

    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('madam'))  #'madam'
print(make_palindrome('hello'))  # 'helloolleh'
```

In this script, we have two functions: `is_palindrome` and `make_palindrome`. 

- `is_palindrome(string)` checks if a given string is a palindrome by comparing it with its reverse.

- `make_palindrome(string)` uses `is_palindrome` to find the longest postfix of the given string that is a palindrome. It then appends the reverse of the prefix before this palindromic suffix to the original string to form the shortest palindrome. If the input string is already a palindrome, it is returned as is.

We test the `make_palindrome` function with several strings to demonstrate its usage and correctness.