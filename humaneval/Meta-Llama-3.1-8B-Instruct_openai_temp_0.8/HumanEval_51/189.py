### Remove Vowels Function
```python
def remove_vowels(text):
    """
    Removes vowels from a given string.

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

# Example usage:
print(remove_vowels('Hello World'))  # Output: 'Hll Wrld'
print(remove_vowels(''))  # Output: ''
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaaaa'))  # Output: ''
print(remove_vowels('aaBAA'))  # Output: 'B'
print(remove_vowels('zbcd'))  # Output: 'zbcd'
```

This script defines the `remove_vowels` function, which takes a string as input and returns the string without vowels. The function uses a list comprehension to iterate over each character in the string, and includes only the characters that are not in the string of vowels. The `join` method is then used to concatenate the characters into a single string. The function is tested with several example inputs to ensure that it works correctly.