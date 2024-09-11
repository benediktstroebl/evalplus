### Remove Vowels from a String
```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.

    Parameters:
    text (str): The input string.

    Returns:
    str: The input string with all vowels removed.
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

This script defines a function `remove_vowels` that takes a string `text` as input. It uses a list comprehension to iterate over each character in the string, checking if the character is not in the string of vowels. The `join` function is then used to combine the characters into a single string without vowels. The function is tested with the provided test cases.