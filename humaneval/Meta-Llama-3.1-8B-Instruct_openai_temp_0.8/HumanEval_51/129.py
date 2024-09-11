```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    Args:
        text (str): The input string.

    Returns:
        str: The input string with all vowels removed.
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the text
    # and then join the characters back into a string
    return ''.join([char for char in text if char not in vowels])

# Test the function
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This Python script defines a function `remove_vowels` that removes all vowels from a given string and returns the resulting string. The function uses a list comprehension to filter out vowels, which are defined as 'aeiouAEIOU'. The test cases at the end of the script demonstrate the function's behavior.