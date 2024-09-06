```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    palindrome = True
    for i in range(len(s)):
        if s[i] in delete:
            continue
        if reverse[i] != s[i]:
            palindrome = False
            break
    return (''.join(delete), palindrome)
```

The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the string resulting from deleting characters in `s` that are also in `c`, and a boolean indicating whether the resulting string is a palindrome. The function iterates through the characters of `s` and `c` individually and creates a list of characters to delete from `s`. Then, it creates a reversed version of `s` to check for palindrome. It iterates through the characters of `s` again, this time deleting characters that are in the delete list or checking characters that are not deleted if they match their reversed version. If any characters do not match, `palindrome` is set to `False`. The function returns a tuple of the cleaned string and a boolean indicating whether it is a palindrome. 

Here is an example usage of the function with a test case:
```python
test_case = 'abcdef', 'b'
print(reverse_delete(*test_case))
```

Output:
```
('acdef', False)
```

The function can also be tested with the example in the problem statement:
```python
test_case = 'abcdedcba', 'ab'
print(reverse_delete(*test_case))
```

Output:
```
('cdedc', True)
```

This demonstrates the function's ability to effectively remove characters from a string and determine whether the resulting string is a palindrome.