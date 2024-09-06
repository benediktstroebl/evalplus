```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test case 1: Empty list
assert concatenate([]) == ''

# Test case 2: Single string
assert concatenate(['a']) == 'a'

# Test case 3: Two strings
assert concatenate(['a', 'b']) == 'ab'

# Test case 4: Three strings
assert concatenate(['a', 'b', 'c']) == 'abc'

# Test case 5: List with spaces
assert concatenate(['a', '   b', 'c']) == 'abc'

# Test case 6: List of strings with special characters
assert concatenate(['$this', '$is', ' awesome']) == '$$is$$ awesome'
```

The function `concatenate` takes a list of strings as input and returns the concatenated string. The function uses the simple concatenation with list comprehension to achieve this. This script also includes a tests to verify the correctness of the `concatenate` function.