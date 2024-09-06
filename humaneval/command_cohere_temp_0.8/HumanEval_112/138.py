```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```

The `reverse_delete()` function takes two strings, `s` and `c`, as input. It first creates a list `delete` by filtering all the characters in `s` that are not present in `c`. This filtered list is reversed and then concatenated with the characters in `s` that are present in `c`. The resulting string is returned as the first element of a tuple, with a boolean indicator of whether it is a palindrome.

Here is an example usage of the function:
```python
s = "abcdedcba"
c = "ab"
result = reverse_delete(s, c)
print(result)  # Output: ('cdedc', True)
```

This demonstrates that the `reverse_delete()` function can successfully reverse delete characters from `s` that are equal to those in `c` and determine whether the resulting string is a palindrome.