```python
def reverse_delete(s, c):
    delete = [char for char in c]
    result = ''.join([char for char in s if char not in delete])
    return result, result == result[::-1]
```
This Python script defines a function called `reverse_delete` taking two strings, `s` and `c` as input. It works by first creating a list comprehension of characters from `c` to delete, then iterating through the characters in `s` and including only the ones not in the delete list. The resulting string is then returned in a tuple with a boolean stating whether it's a palindrome or not, by checking if it's equal to its reversed version. This solves the problem of removing characters from `s` that are also in `c`, and determining if the resulting string is a palindrome.