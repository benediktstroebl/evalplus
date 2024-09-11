```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string from which vowels are to be removed.
    
    Returns:
    str: The string after removing all vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Testing the function
print(remove_vowels(''))  # Expected Output: ''
print(remove_vowels("abcdef\nghijklm"))  # Expected Output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Expected Output: 'bcdf'
print(remove_vowels('aaaaa'))  # Expected Output: ''
print(remove_vowels('aaBAA'))  # Expected Output: 'B'
print(remove_vowels('zbcd'))  # Expected Output: 'zbcd'
```

In this script, we use a list comprehension to create a new list that includes all characters from the input string except for vowels. The `join` method is then used to concatenate these characters into a single string. This string is then returned as the result.