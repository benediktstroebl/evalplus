```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string
    
    Returns:
    str: The input string without vowels
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

In this code, the `remove_vowels` function uses a list comprehension to filter out vowels from the input string. The `join` method is used to concatenate the characters back into a string. The vowels to be removed are defined in the `vowels` string, which includes both lowercase and uppercase vowels.