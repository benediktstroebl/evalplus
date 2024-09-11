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
print(remove_vowels('')) # ''
print(remove_vowels("abcdef\nghijklm")) # 'bcdf\nghjklm'
print(remove_vowels('abcdef')) # 'bcdf'
print(remove_vowels('aaaaa')) # ''
print(remove_vowels('aaBAA')) # 'B'
print(remove_vowels('zbcd')) # 'zbcd'
```

This script uses a list comprehension to iterate over each character in the input string. If the character is not a vowel, it's included in the new string. The `join()` function is then used to concatenate all the characters into a single string.