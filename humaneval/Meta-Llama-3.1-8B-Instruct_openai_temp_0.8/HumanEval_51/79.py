### Remove Vowels from a String
#### A Python Script
```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Parameters:
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
print(remove_vowels(''))  # Output: ''
print(remove_vowels("abcdef\nghijklm"))  # Output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaaaa'))  # Output: ''
print(remove_vowels('aaBAA'))  # Output: 'B'
print(remove_vowels('zbcd'))  # Output: 'zbcd'
```
This script defines a function `remove_vowels` that uses a list comprehension to filter out vowels from the input string. The `join` method is then used to concatenate the remaining characters back into a string.