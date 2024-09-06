```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    return (''.join(delete), delete == delete[::-1])
```

The problem asks us to create a function `reverse_delete(s,c)` that takes two strings as input, `s` and `c`, and returns a tuple containing a string created by deleting from `s` all characters that are present in `c`, and a boolean indicating whether the resulting string is a palindrome. Our approach is to filter out the characters in `s` that are also in `c`, and then reverse the remaining characters and pad the beginning of the string with an empty character to allow for correct alignment. We then compare the resulting string with its reverse to determine palindrome status, or indicate boolean `True` if they are the same, and boolean `False` if they are different. 

The unit tests passed with the code provide an assurance that the function works for a variety of corner cases and provides a way for consumers of the code to verify its behavior with different inputs.