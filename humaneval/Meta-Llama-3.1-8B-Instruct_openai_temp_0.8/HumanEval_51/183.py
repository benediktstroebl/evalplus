### Remove Vowels from a String
```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    # Define the vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels
    # The `if char not in vowels` condition ensures only non-vowel characters are included
    no_vowels = [char for char in text if char not in vowels]
    
    # Join the filtered characters into a single string
    result = ''.join(no_vowels)
    
    return result

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```
This script defines a function `remove_vowels` that takes a string `text` as input and returns the string without vowels. It uses a list comprehension to filter out vowels and then joins the filtered characters into a single string using `''.join()`. The test cases at the end verify that the function behaves as expected.