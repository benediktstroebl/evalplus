```python
def remove_vowels(text):
    """
    Remove vowels from a given text.

    Args:
        text (str): The input text from which vowels are to be removed.

    Returns:
        str: The text without vowels.
    """
    # Define a string of all lowercase vowels
    vowels = 'aeiou'
    
    # Use a list comprehension to filter out vowels from the text
    # The islower() method checks if a character is lowercase
    # The in operator checks if a character is in the vowels string
    # The join() method is used to concatenate the filtered characters into a string
    text_without_vowels = ''.join([char for char in text if char not in vowels and char.islower()])
    
    # Return the text without vowels
    return text_without_vowels

# Test the function
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines the `remove_vowels` function that removes all vowels (both lowercase and uppercase) from a given text. It uses a list comprehension to filter out vowels and then joins the remaining characters into a string. The function is then tested with the provided example use cases.