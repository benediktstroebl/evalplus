```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test case: Concatenate empty list
print(concatenate([]))

# Test case: Concatenate list of strings
print(concatenate(['a', 'b', 'c']))
```
This script defines a function **concatenate** that takes a list of strings as input and returns the concatenated string. The function uses the string formatting to create a single string by concatenating the input list. The test cases demonstrate the **empty list** and a list of strings, passing them to the function and printing the result. 

This script is self-contained and does not require any additional imports or external functions.