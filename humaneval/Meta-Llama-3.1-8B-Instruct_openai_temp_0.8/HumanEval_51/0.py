### Remove Vowels from a String
#### Python Script
```markdown
### remove_vowels.py

```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
    text (str): The input string.

    Returns:
    str: The string without vowels.
    """
    # Define vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels
    # and then join the characters back into a string
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

### Usage
To use this script, save it as `remove_vowels.py` and run it using Python: `python remove_vowels.py`. You can also import the `remove_vowels` function into your own Python code and use it as needed.
```python
from remove_vowels import remove_vowels

print(remove_vowels('hello world'))  # 'hll wrld'
```