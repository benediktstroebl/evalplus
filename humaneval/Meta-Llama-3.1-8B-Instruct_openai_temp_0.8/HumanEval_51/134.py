```python
def remove_vowels(text):
    """
    Remove vowels from the given text.

    Args:
        text (str): The input string.

    Returns:
        str: The input string without vowels.
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

This script defines a function `remove_vowels` that takes a string as input and returns a new string with all vowels removed. It uses a list comprehension to iterate over each character in the input string, checks if the character is a vowel (case-insensitive), and if not, includes it in the new string. The resulting string is then returned.

The script also includes the test cases specified in the problem description to demonstrate the function's behavior.