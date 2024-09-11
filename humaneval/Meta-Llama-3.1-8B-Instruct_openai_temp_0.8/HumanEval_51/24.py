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
    
    # Use a list comprehension to filter out vowels from the input string
    # The if condition checks if a character is not in the vowels string
    # The result is a list of characters without vowels
    result = [char for char in text if char not in vowels]
    
    # Join the list of characters into a string
    result = ''.join(result)
    
    return result

# Test the function
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines a function `remove_vowels` that takes a string as input, removes all vowels from the string, and returns the resulting string. The function uses a list comprehension to filter out vowels from the input string and then joins the resulting list of characters back into a string. The script also includes test cases to verify that the function works as expected.