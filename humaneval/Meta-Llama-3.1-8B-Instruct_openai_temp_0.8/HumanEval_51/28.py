### Remove Vowels from a String

Here's a Python function that removes vowels from a given string. This function is case-sensitive and considers 'y' as a consonant.

```markdown
### Code
```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The input string with vowels removed.
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the input string
    # The `if char not in vowels` condition ensures that only non-vowel characters are included
    filtered_text = [char for char in text if char not in vowels]
    
    # Join the filtered characters into a single string
    result = ''.join(filtered_text)
    
    return result

# Example usage:
print(remove_vowels(""))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

### Explanation

This script defines a function `remove_vowels` that takes a string `text` as input. It uses a list comprehension to create a new list that includes only the characters from `text` that are not vowels. The `if char not in vowels` condition filters out vowels (both lowercase and uppercase). The filtered characters are then joined into a single string using the `join` method. The function returns this string.

You can run this script to test the function with the provided example inputs.