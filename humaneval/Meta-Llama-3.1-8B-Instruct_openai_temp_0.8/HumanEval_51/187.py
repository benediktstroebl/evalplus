```python
def remove_vowels(text):
    """
    Removes vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    # Define the set of vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Use a generator expression to filter out vowels
    # The join function is used to concatenate the characters back into a string
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script defines a function `remove_vowels` that takes a string as input and returns a string without vowels. It uses a set of vowels and a generator expression to efficiently filter out the vowels from the input string. The test cases at the end demonstrate the function's behavior with different inputs. 

Alternatively, you can use regular expressions to achieve the same result:

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
    # Use a regular expression to replace vowels with an empty string
    return re.sub('[aeiouAEIOU]', '', text)

# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This version uses the `re.sub` function to replace all occurrences of vowels with an empty string, effectively removing them from the input string.