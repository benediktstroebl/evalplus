```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reversed_s = s[:0]
    for i, char in enumerate(s):
        if char not in delete:
            reversed_s = reversed_s + char
    reversed_s = reversed(reversed_s)
    return (reversed_s, reversed_s == s)
```

The function `reverse_delete()` takes two strings `s` and `c` as input and returns a tuple containing the result string and a boolean indicating if the check is a palindrome. The deletion process is done in two main steps:
1. Create a list `delete` that contains all the characters from string `c`.
2. Use a temporary variable `reversed_s` to build the reversed string, deleting characters from `s` that are not in `delete`. 

Then the function checks if the resulting string is a palindrome.