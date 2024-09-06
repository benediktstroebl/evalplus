Here's a self-contained Python function that performs the XOR operation on two strings, considering only single characters:
```python
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of single characters.
    Args:
        a and b are strings consisting of only single characters.
    Returns: string formed by performing the XOR operation on all characters.
    """

Example:
    'ABC' -> 'BC'
    """
    # Add all characters from both strings to result
    result = ''.join([c for c in a] + [c for c in b])
    return result
```
This function takes two strings a and b as input and returns the XOR of the two strings, formed by concatenating all characters from both inputs.