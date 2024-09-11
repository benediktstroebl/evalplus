### Remove Vowels Function
```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string with vowels removed.
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
This script defines a function `remove_vowels` that takes a string as input and returns the string with all vowels removed. It uses a list comprehension to iterate over each character in the input string, checking if it's a vowel by looking it up in the string `vowels`. If it's not a vowel, the character is included in the new string. The resulting string is then returned.