```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Args:
        text (str): The input string.
    
    Returns:
        str: The input string with all vowels removed.
    
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


# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script defines a function `remove_vowels` that takes a string as input and returns a new string with all vowels removed. The function uses a list comprehension to iterate over each character in the input string, and includes only the characters that are not vowels. The resulting list of characters is then joined back into a string using the `join` method. The script also includes test cases to demonstrate the function's behavior.