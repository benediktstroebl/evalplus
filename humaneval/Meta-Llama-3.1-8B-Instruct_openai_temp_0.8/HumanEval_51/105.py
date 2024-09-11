```python
def remove_vowels(text):
    """
    Remove vowels from a given string.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The string without vowels.
    """
    # Define the set of vowels
    vowels = set('aeiouAEIOU')
    
    # Use a generator expression to filter out vowels
    # and join the remaining characters back into a string
    return ''.join([char for char in text if char not in vowels])

# Test the function
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script uses a set of vowels to efficiently filter out characters from the input string. The `join` method is used to combine the filtered characters back into a string. This approach is more memory-efficient than generating a new string by concatenating characters, especially for large input strings.