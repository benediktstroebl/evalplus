```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The input string without vowels.
    
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
print(remove_vowels(''))  # Expected output: ''
print(remove_vowels("abcdef\nghijklm"))  # Expected output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Expected output: 'bcdf'
print(remove_vowels('aaaaa'))  # Expected output: ''
print(remove_vowels('aaBAA'))  # Expected output: 'B'
print(remove_vowels('zbcd'))  # Expected output: 'zbcd'
```