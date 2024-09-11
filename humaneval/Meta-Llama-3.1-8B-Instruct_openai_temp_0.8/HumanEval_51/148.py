```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    Parameters:
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

This script defines a function `remove_vowels` that takes a string `text` as input and returns a new string with all vowels removed. The `vowels` string contains all vowels (both lowercase and uppercase). The list comprehension iterates over each character in the input string and includes it in the new string only if it is not in the `vowels` string. The `join` method is then used to concatenate the characters into a single string.