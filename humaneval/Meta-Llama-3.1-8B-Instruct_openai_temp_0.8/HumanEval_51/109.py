```python
def remove_vowels(text):
    """
    Remove all vowels from a given string.

    Args:
    text (str): The input string.

    Returns:
    str: The string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines a function `remove_vowels` that takes a string `text` as input and returns a new string without any vowels. It uses a list comprehension to create a new string that includes only the characters that are not vowels. The test cases at the end of the script verify that the function behaves as expected.