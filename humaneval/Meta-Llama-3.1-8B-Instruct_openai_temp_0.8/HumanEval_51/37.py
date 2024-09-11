```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The string without vowels.
    
    """
    # Define the vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out the vowels from the text
    # The if condition checks if the character is not in the vowels string
    filtered_text = [char for char in text if char not in vowels]
    
    # Join the filtered list of characters into a string
    result = ''.join(filtered_text)
    
    return result

# Test the function with the provided examples
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script defines a function called `remove_vowels` that takes a string as input and returns a new string without vowels. It uses a list comprehension to filter out the vowels, and then joins the remaining characters into a string. The function is then tested with the provided examples.