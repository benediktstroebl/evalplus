### Remove Vowels from a String
#### Python Script
```markdown
### remove_vowels.py
```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.

    Examples:
        >>> remove_vowels('')
        ''
        >>> remove_vowels("abcdef\nghijklm")
        'bcdf\nghjklm'
        >>> remove_vowels('abcdef')
        'bcdf'
        >>> remove_vowels('aaaaa')
        ''
        >>> remove_vowels('aaBAA')
        'B'
        >>> remove_vowels('zbcd')
        'zbcd'
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Example usage
if __name__ == "__main__":
    print(remove_vowels('hello world'))
```

This script defines the `remove_vowels` function which takes a string `text` as input, removes all vowels from it, and returns the resulting string. It uses a list comprehension to create a list of characters that are not vowels, and then joins this list into a string using the `join` method.

The example usage at the end of the script demonstrates how to use the `remove_vowels` function to remove vowels from a string.