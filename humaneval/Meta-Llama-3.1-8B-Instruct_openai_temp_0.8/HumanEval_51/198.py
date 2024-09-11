```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
    text (str): The input string.

    Returns:
    str: The input string without vowels.
    """
    # Define vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels
    # The if condition checks if a character is not in the vowels string
    # Then use the join function to convert the list back into a string
    return ''.join([char for char in text if char not in vowels])

# Test the function
print(remove_vowels(''))  # Should print an empty string
print(remove_vowels("abcdef\nghijklm"))  # Should print 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Should print 'bcdf'
print(remove_vowels('aaaaa'))  # Should print an empty string
print(remove_vowels('aaBAA'))  # Should print 'B'
print(remove_vowels('zbcd'))  # Should print 'zbcd'
```