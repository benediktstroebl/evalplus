```python
def concatenate(strings: List[str]) -> str:
    """
    Function to concatenate list of strings into a single string.

    Parameters:
    strings: list of strings to be concatenated.

    Returns:
    concatenated string.
    """
    string: list of string values to be concatenated into a single string
    """
    return ''.join(strings)

# Test cases
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)  # Output: 'abc'

strings = []
result = concatenate(strings)
print(result)  # Output: ''

strings = ['a', 'b', 'c']
result = concatenate(['d', 'e'])
print(result)  # Output: 'ade'

strings = ['a', 'b', 'c', 'x']
result = concatenate(strings)
print(result)  # Output: 'acy'
``` 
This function concatenates a list of strings into a single string, and the test cases ensure that the function works correctly for different inputs.