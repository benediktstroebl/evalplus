```python
def remove_vowels(text):
    """
    Removes vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    # Define the set of vowels
    vowels = set('aeiouAEIOU')

    # Use a list comprehension to create a new string without vowels
    # The `if char not in vowels` condition filters out vowels
    # The `join()` method concatenates the characters back into a string
    return ''.join([char for char in text if char not in vowels])

# Test the function
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

Alternatively, you can use the `re` module's `sub()` function to replace vowels with an empty string:

```python
import re

def remove_vowels(text):
    """
    Removes vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    return re.sub('[aeiouAEIOU]', '', text)

# Test the function
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```