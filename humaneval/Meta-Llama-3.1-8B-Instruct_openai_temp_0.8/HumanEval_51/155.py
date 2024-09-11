```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Args:
        text (str): Input string.
    
    Returns:
        str: Input string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This Python script defines a function `remove_vowels` that takes a string as input and returns the string without vowels. It uses a list comprehension to iterate over each character in the string, checks if the character is not a vowel, and then joins the resulting characters into a new string. The test cases are provided at the end of the script to verify the function's correctness.