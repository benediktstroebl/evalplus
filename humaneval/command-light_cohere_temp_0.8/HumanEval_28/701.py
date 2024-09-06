```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: concatenated string
    """
    if not strings:
        return ''
    return ''.join(strings)

# Additional test cases for function correctness
# Add your tests here

# Example usage
result = concatenate(['a', 'b', 'c'])
print(result)  # Output: 'abc'
```
This code provides a function `concatenate` that takes a list of strings as input and returns the concatenated string. You can add more test cases to cover different scenarios to ensure the function behaves correctly.