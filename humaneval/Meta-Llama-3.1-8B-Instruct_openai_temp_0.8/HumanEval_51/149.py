```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string to remove vowels from.
    
    Returns:
    str: The input string with all vowels removed.
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to iterate over each character in the string
    # and include it in the new string if it's not a vowel
    return ''.join([char for char in text if char not in vowels])

# Test the function
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines a function `remove_vowels` that takes a string `text` as input and returns the string with all vowels removed. It uses a list comprehension to iterate over each character in the string, including it in the new string if it's not a vowel. The `join` method is then used to concatenate the characters in the list into a single string.