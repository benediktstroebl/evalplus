```markdown
### Remove Vowels From a String

#### Code

```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
if __name__ == "__main__":
    print(remove_vowels(''))
    print(remove_vowels("abcdef\nghijklm"))
    print(remove_vowels('abcdef'))
    print(remove_vowels('aaaaa'))
    print(remove_vowels('aaBAA'))
    print(remove_vowels('zbcd'))
```

#### How It Works

This script defines a function `remove_vowels` that takes a string as input and returns a new string with all vowels removed.

- The function uses a string `vowels` to store all the vowels (both lowercase and uppercase).
- It uses a list comprehension to generate a new list of characters that are not in the `vowels` string.
- The `join` method is then used to concatenate the characters in the list into a single string.
```