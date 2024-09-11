```python
def remove_vowels(text):
    """
    Removes all vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The input string without vowels.
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

This script defines a function `remove_vowels` that takes a string `text` as input and returns a new string with all vowels removed. It uses a list comprehension to iterate over each character in the string, and only includes characters that are not vowels (i.e., characters that are not in the string `'aeiouAEIOU'`). The resulting list of characters is then joined back into a string using the `join` method. The test cases at the end of the script demonstrate the function's behavior.