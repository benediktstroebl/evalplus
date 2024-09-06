```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test case 1
strings = []
result = concatenate(strings)
print("Test case 1 result:", result)  # Output: ''

# Test case 2
strings = ['a', 'b', 'c']
result = concatenate(strings)
print("Test case 2 result:", result)  # Output: 'abc'

# Test case 3
strings = ['123']
result = concatenate(strings)
print("Test case 3 result:", result)  # Output: '123'

# Test case 4
strings = ['a', 'b', 'c', 'd']
result = concatenate(strings)
print("Test case 4 result:", result)  # Output: 'abcd'
```
The function concatenate in this version accepts a list of strings as an argument and outputs a single string by joining the strings. The test cases demonstrate that this function may be used successfully.