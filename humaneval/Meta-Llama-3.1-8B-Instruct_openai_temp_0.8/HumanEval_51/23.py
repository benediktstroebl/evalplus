```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The input string with all vowels removed.
    """
    # Define a string of vowels (both lowercase and uppercase) to check against
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the input string
    # The join method is then used to concatenate the characters back into a string
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # Expected output: ''
print(remove_vowels("abcdef\nghijklm"))  # Expected output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Expected output: 'bcdf'
print(remove_vowels('aaaaa'))  # Expected output: ''
print(remove_vowels('aaBAA'))  # Expected output: 'B'
print(remove_vowels('zbcd'))  # Expected output: 'zbcd'
```

This script defines a function `remove_vowels` that takes a string as input and returns a string with all vowels removed. The function uses a list comprehension to filter out vowels from the input string, and the `join` method is used to concatenate the characters back into a string. The test cases are included at the end to verify the function's correctness.