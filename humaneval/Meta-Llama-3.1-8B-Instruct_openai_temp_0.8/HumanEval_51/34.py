### Remove Vowels from a String
#### Python Function

```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.

    Args:
        text (str): The input string.

    Returns:
        str: The input string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])


# Test cases
if __name__ == "__main__":
    print(remove_vowels(''))  # ''
    print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
    print(remove_vowels('abcdef'))  # 'bcdf'
    print(remove_vowels('aaaaa'))  # ''
    print(remove_vowels('aaBAA'))  # 'B'
    print(remove_vowels('zbcd'))  # 'zbcd'
```

### Explanation

This script defines a function `remove_vowels` that takes a string `text` and returns a new string with all vowels removed. The function uses a list comprehension to iterate over each character in the input string, and only includes the character in the output string if it is not a vowel.

The test cases at the end of the script ensure that the function behaves correctly in different scenarios.