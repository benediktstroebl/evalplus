```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test cases
my_strings = ['a', 'b', 'c']
result = concatenate(my_strings)
print("Result:", result)  # Output: 'abc'

empty_strings = []
result = concatenate(empty_strings)
print("Result:", result)  # Output: ''

long_strings = ['a', 'b', 'c', 'd', 'e']
result = concatenate(long_strings)
print("Result:", result)  # Output: 'ade'
```
The above Python script defines a function called `concatenate` that takes a list of strings as input and returns the concatenated string. It then passes these test cases and prints the results.