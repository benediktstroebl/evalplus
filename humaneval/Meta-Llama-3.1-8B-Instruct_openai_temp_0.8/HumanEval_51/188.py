```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Args:
        text (str): The input string.
    
    Returns:
        str: The input string without vowels.
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to create a new string without vowels
    # The if condition checks if the character is not a vowel
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines a function `remove_vowels` that takes a string `text` as input and returns the string without vowels. It uses a list comprehension to iterate over the characters in the input string and creates a new string that includes only the characters that are not vowels (defined as 'aeiouAEIOU'). The resulting string is then returned. The script also includes the test cases provided in the problem statement to demonstrate that the function works correctly.