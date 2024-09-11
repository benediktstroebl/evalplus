```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string from which vowels are to be removed.
    
    Returns:
    str: The string without vowels.
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

This script defines a function `remove_vowels` that takes a string as input, removes all the vowels (both lowercase and uppercase) from the string, and returns the resulting string. The test cases are used to verify the correctness of the function.