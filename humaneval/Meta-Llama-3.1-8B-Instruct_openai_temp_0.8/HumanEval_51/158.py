```python
def remove_vowels(text):
    """
    Remove all vowels from a given string.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The string with all vowels removed.
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the input string
    # The `join` function is used to convert the list back into a string
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```