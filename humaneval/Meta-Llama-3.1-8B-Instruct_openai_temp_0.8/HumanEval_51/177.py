```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string
    
    Returns:
    str: The string without vowels
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # Output: ''
print(remove_vowels("abcdef\nghijklm"))  # Output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaaaa'))  # Output: ''
print(remove_vowels('aaBAA'))  # Output: 'B'
print(remove_vowels('zbcd'))  # Output: 'zbcd'
```

This script defines a function `remove_vowels` that takes a string `text` as input and returns the string with all vowels removed. It uses a list comprehension to filter out the vowels and then joins the remaining characters back into a string. The test cases are included at the end to verify the function's correctness.