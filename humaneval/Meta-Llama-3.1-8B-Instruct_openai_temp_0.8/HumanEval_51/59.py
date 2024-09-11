```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): Input string
    
    Returns:
    str: String without vowels
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the input string
    # The translate method is not used because it requires additional steps to create a translation table
    # and to translate the string back, which makes the code more complex
    result = ''.join([char for char in text if char not in vowels])
    
    return result

# Test the function
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script uses a list comprehension to filter out vowels from the input string. This approach is concise and efficient, as it avoids the need to create a translation table or to translate the string back after filtering.