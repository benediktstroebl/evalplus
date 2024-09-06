Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test case 1
test_strlen = {method: strlen, args: '', raises: ValueError}

# Test case 2
test_strlen = {method: strlen, args: 'abc', raises: ValueError}

# Test case 3
test_strlen = {method: strlen, args: 'abc123'}
```
This code defines a function called `strlen`, which takes a string as input and returns its length. The function uses the simplicity by leveraging Python's `len()` function, which directly returns the length of the given string. The code also provides test cases to ensure that the `strlen` function works correctly for different inputs.