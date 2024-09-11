```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The input string without vowels.
    """
    vowels = 'aeiouAEIOU'  # Define the vowels to be removed
    return ''.join([char for char in text if char not in vowels])  # Use list comprehension to filter out vowels


# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This Python script uses a list comprehension to filter out the vowels from the input string. The `join()` function is then used to concatenate the remaining characters back into a string. The test cases are included to verify the correctness of the function.