```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string from which vowels are to be removed.
    
    Returns:
    str: The input string without vowels.
    """
    # Use a list comprehension to filter out vowels
    # The 'if' condition checks if a character is not a vowel
    # The 'join' function is used to concatenate the characters back into a string
    text_without_vowels = ''.join([char for char in text if char.lower() not in 'aeiou'])
    
    return text_without_vowels

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines the `remove_vowels` function, which filters out vowels from the input string and returns the resulting string. The function uses a list comprehension to iterate over each character in the input string, and checks if the character is not a vowel (case-insensitive). If the character is not a vowel, it is included in the new string. Finally, the `join` function is used to concatenate the characters back into a string, which is returned by the function. The script then includes the test cases from the problem statement to demonstrate the functionality of the `remove_vowels` function.