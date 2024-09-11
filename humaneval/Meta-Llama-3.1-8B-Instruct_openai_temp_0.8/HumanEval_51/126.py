```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string
    
    Returns:
    str: The input string without vowels
    """
    # Define the vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the input string
    # The if condition checks if each character is not in the vowels string
    # The join function is used to concatenate the characters back into a string
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script defines a function `remove_vowels` that takes a string as input and returns the string without vowels. The function uses a list comprehension to filter out vowels from the input string. It uses the `join` function to concatenate the characters back into a string. The test cases are included at the end of the script to verify that the function works correctly.