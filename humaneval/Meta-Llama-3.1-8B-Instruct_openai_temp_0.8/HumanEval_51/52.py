```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The input string without vowels.
    """
    # Define a set of vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Use a list comprehension to create a new string without vowels
    # The expression [char for char in text if char not in vowels] 
    # iterates over each character in the input string and only includes it in the new string if it's not a vowel
    # The join() function is used to concatenate the characters in the list into a single string
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```