### Remove Vowels Function
```python
def remove_vowels(text):
    """
    Remove all vowels from a given string.

    Args:
    text (str): The input string from which vowels are to be removed.

    Returns:
    str: The input string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Example usage:
if __name__ == "__main__":
    print(remove_vowels(''))  # ''
    print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
    print(remove_vowels('abcdef'))  # 'bcdf'
    print(remove_vowels('aaaaa'))  # ''
    print(remove_vowels('aaBAA'))  # 'B'
    print(remove_vowels('zbcd'))  # 'zbcd'
```