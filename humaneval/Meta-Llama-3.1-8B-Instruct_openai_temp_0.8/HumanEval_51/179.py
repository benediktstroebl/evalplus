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
print(remove_vowels('')) # ''
print(remove_vowels("abcdef\nghijklm")) # 'bcdf\nghjklm'
print(remove_vowels('abcdef')) # 'bcdf'
print(remove_vowels('aaaaa')) # ''
print(remove_vowels('aaBAA')) # 'B'
print(remove_vowels('zbcd')) # 'zbcd'
```

This script uses a list comprehension to create a new string where each character is included if it is not a vowel. The `join()` method is then used to concatenate the characters in the list into a single string.