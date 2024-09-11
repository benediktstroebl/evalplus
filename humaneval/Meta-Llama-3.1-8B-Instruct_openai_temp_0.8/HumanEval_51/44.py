```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.

    Examples:
        >>> remove_vowels('')
        ''
        >>> remove_vowels("abcdef\nghijklm")
        'bcdf\nghjklm'
        >>> remove_vowels('abcdef')
        'bcdf'
        >>> remove_vowels('aaaaa')
        ''
        >>> remove_vowels('aaBAA')
        'B'
        >>> remove_vowels('zbcd')
        'zbcd'
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test the function with the provided examples
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines a function `remove_vowels` that takes a string as input and returns a new string with all vowels removed. The function uses a list comprehension to iterate over each character in the string, and the `join` method to concatenate the characters back into a string. The test cases at the end of the script demonstrate the function's behavior with the provided examples.