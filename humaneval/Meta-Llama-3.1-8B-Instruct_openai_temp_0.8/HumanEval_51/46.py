```python
def remove_vowels(text):
    """
    Removes all vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string with all vowels removed.
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

This script defines a function `remove_vowels` that takes a string as input and returns the string with all vowels removed. It uses a list comprehension to iterate over each character in the string, checking if it's a vowel using the string `vowels`. If it's not a vowel, the character is included in the new string. The `join` method is used to concatenate the characters back into a single string.