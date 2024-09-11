```markdown
### Remove Vowels from a String
#### Python Function to Remove Vowels from a Given Text
```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string from which vowels are to be removed.
    
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
    # Define vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the text
    # The `filter()` function and `join()` method are used to remove vowels
    # The `str.translate()` method is an efficient way to remove specific characters from a string
    text_without_vowels = text.translate(str.maketrans('', '', vowels))
    
    return text_without_vowels

# Test the function with some examples
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This Python script defines a function `remove_vowels` that takes a string as input and returns the string without vowels. It uses the `str.translate()` method to efficiently remove vowels from the text. The `str.maketrans()` method is used to create a translation table that maps vowels to None (i.e., removes them). The script includes docstrings and test cases to demonstrate the function's behavior.