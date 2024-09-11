```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
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
    # Define vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the string
    # The if condition checks if a character is not in the vowels string
    text_without_vowels = ''.join([char for char in text if char not in vowels])
    
    return text_without_vowels

# Test the function
print(remove_vowels(''))  # Output: ''
print(remove_vowels("abcdef\nghijklm"))  # Output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaaaa'))  # Output: ''
print(remove_vowels('aaBAA'))  # Output: 'B'
print(remove_vowels('zbcd'))  # Output: 'zbcd'
```