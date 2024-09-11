```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The string without vowels.
    
    Example:
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
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the input string
    # The if condition checks if the character is not in the vowels string
    # The resulting list of characters is then joined back into a string
    return ''.join([char for char in text if char not in vowels])

# Test the function
print(remove_vowels(""))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

In this script, the `remove_vowels` function uses a list comprehension to iterate over each character in the input string. If a character is not a vowel (i.e., it's not in the `vowels` string), it's included in the new string. The resulting list of characters is then joined back into a string using the `''.join()` method. The function is tested with the provided example strings.