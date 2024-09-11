```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
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
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to iterate over the input string and 
    # include only characters that are not vowels
    text_without_vowels = [char for char in text if char not in vowels]
    
    # Join the list of characters back into a string
    return ''.join(text_without_vowels)

# Test the function with some examples
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script defines a function `remove_vowels` that removes all vowels from a given string. It uses a list comprehension to iterate over the input string and includes only characters that are not vowels. The list of characters is then joined back into a string using the `''.join()` method. The function is tested with some examples to demonstrate its behavior.