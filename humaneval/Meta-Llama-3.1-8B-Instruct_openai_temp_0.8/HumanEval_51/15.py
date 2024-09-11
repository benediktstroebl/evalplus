```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The input string without vowels.
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the input string
    # The `join()` function is then used to concatenate the filtered characters into a string
    filtered_text = ''.join([char for char in text if char not in vowels])
    
    return filtered_text

# Test the function with the provided test cases
print(remove_vowels(''))       # Expected output: ''
print(remove_vowels("abcdef\nghijklm"))  # Expected output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Expected output: 'bcdf'
print(remove_vowels('aaaaa'))  # Expected output: ''
print(remove_vowels('aaBAA'))  # Expected output: 'B'
print(remove_vowels('zbcd'))  # Expected output: 'zbcd'
```

This script defines the `remove_vowels()` function, which takes a string as input and returns a new string with all vowels removed. The script then includes test cases to verify the function's correctness. The function uses a list comprehension to filter out vowels from the input string, which is a concise and efficient way to solve this problem.