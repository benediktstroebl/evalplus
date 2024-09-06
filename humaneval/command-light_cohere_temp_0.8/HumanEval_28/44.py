```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return "".join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print("Result:", result)  # Output: abc

strings = []
result = concatenate(strings)
print("Result:", result)  # Output: ""

strings = ["a", "b", "c", "d"]
result = concatenate(strings)
print("Result:", result)  # Output: abcdd
``` 
This code defines a function called `concatenate` that takes a list of strings as an argument and returns the concatenated string. It then tests this strings list with a few different permutations to ensure the function works as expected.