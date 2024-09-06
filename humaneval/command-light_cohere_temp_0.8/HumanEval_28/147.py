```python
def concatenate(strings: List[str]) -> str:
    """
    Combine all strings into a single string.
    Args:
    strings: list of strings
    Returns:
        joined string
    """
    return ''.join(strings)

# Test the function with various inputs
test_strings = ['a', 'b', 'c']
result = concatenate(test_strings)
print(result)  # Output: 'abc'
```
The code defines a function called **concatenate** that takes a list of strings as an argument and returns the concatenated string. It then tests this strings list with various contents and prints the result, which will be the string "abc" in this case.