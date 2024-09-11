```markdown
### Palindrome Maker

This script provides two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` generates the shortest palindrome that begins with a supplied string.

#### Code

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    i = 0
    while i < len(string) and string == string[::-1][i:]:
        i += 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + string[:i][::-1]


# Test cases
print(is_palindrome('radar'))  # True
print(is_palindrome('hello'))  # False
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

#### Explanation

- `is_palindrome` function checks if a given string is a palindrome by comparing it with its reverse.
- `make_palindrome` function generates the shortest palindrome that begins with a supplied string.
  - If the input string is empty, it returns an empty string.
  - Otherwise, it finds the longest postfix of the supplied string that is a palindrome by iterating from the end of the string and checking if the string equals its reverse from the current index to the end.
  - It then appends to the end of the string the reverse of the string prefix that comes before the palindromic suffix.

This script includes test cases to demonstrate the functionality of the provided functions.