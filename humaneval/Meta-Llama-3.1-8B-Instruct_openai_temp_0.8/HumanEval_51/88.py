### Remove Vowels from a String
#### Problem Description

This script defines a function `remove_vowels` that takes a string as input and returns the string without vowels.
#### Solution

```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string
    
    Returns:
    str: The input string without vowels
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to create a new string without vowels
    # The `if char not in vowels` condition filters out vowels from the string
    text_without_vowels = ''.join([char for char in text if char not in vowels])
    
    return text_without_vowels

# Example use cases
print(remove_vowels(''))  # Output: ''
print(remove_vowels("abcdef\nghijklm"))  # Output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaaaa'))  # Output: ''
print(remove_vowels('aaBAA'))  # Output: 'B'
print(remove_vowels('zbcd'))  # Output: 'zbcd'
```

This script defines the function `remove_vowels` as described in the problem statement. It uses a list comprehension to create a new string without vowels and returns this new string. The example use cases demonstrate the function's behavior with different inputs.