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

# Test the function
if __name__ == "__main__":
    print(remove_vowels(""))
    print(remove_vowels("abcdef\nghijklm"))
    print(remove_vowels('abcdef'))
    print(remove_vowels('aaaaa'))
    print(remove_vowels('aaBAA'))
    print(remove_vowels('zbcd'))
```

This script defines a function `remove_vowels` that takes a string as input and returns a new string with all vowels removed. The function uses a list comprehension to iterate over each character in the input string, and only includes characters that are not vowels. The `join` function is then used to concatenate the characters back into a string. The function is tested with the example use cases provided.