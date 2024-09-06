```python
def strlen(string: str) -> int:
    """ Returns length of given string"""
    return len(string)

# Test case 1:
assert strlen('') == 0

# Test case 2:
assert strlen('abc') == 3
```

The provided code defines a function `strlen` that calculates and returns the length of a given string. The function uses the straightforward Python's `len()` function to get the length of the string passed as an argument. 

The code also comes with two test cases, `test case 1` and `test case 2`, that verify the function's behavior for empty strings and the length of the alphabet 'abc'.