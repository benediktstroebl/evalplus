```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): Input string.
    
    Returns:
    str: Input string without vowels.
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

In this script, we define a function `remove_vowels` that uses list comprehension to create a new string without vowels. We use the `join` method to concatenate the characters in the list into a single string. The `vowels` string contains all the vowels (both lowercase and uppercase) that we want to remove. The function returns this new string.

The test cases at the end demonstrate the function's behavior with different inputs.