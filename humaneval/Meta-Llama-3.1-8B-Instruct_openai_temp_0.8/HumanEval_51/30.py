```python
def remove_vowels(text):
    """
    Removes vowels from a given string.

    Args:
    text (str): The input string.

    Returns:
    str: The string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script defines a function `remove_vowels` that takes a string and returns the string with all vowels (both lowercase and uppercase) removed. The test cases at the end demonstrate the function's behavior with different inputs.