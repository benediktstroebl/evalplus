```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Args:
        text (str): The input string.
    
    Returns:
        str: The input string without vowels.
    """
    vowels = 'aeiouAEIOU'  # Define the vowels to be removed
    return ''.join([char for char in text if char not in vowels])  # Use list comprehension to generate the new string


# Test the function
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script uses a list comprehension to generate a new string without vowels, and the `''.join()` function to concatenate the characters back into a string.