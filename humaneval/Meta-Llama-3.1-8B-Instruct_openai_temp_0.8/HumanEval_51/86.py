### Remove Vowels Function
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
    # Define the set of vowels in both lowercase and uppercase
    vowels = set('aeiouAEIOU')
    
    # Use a list comprehension to filter out vowels from the string
    # and then join the characters back into a string
    return ''.join([char for char in text if char not in vowels])

# Test the function
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```