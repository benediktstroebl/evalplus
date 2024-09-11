### Removing Vowels from a String
Below is a Python script that accomplishes the task. This function `remove_vowels` takes a string as input and returns a new string without any vowels (both lowercase and uppercase).

```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.

    Args:
        text (str): The input string.

    Returns:
        str: The input string without vowels.

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
    # Vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    # Use a list comprehension to filter out vowels
    return ''.join([char for char in text if char not in vowels])

# Example usage
if __name__ == "__main__":
    print(remove_vowels(''))  # ''
    print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
    print(remove_vowels('abcdef'))  # 'bcdf'
    print(remove_vowels('aaaaa'))  # ''
    print(remove_vowels('aaBAA'))  # 'B'
    print(remove_vowels('zbcd'))  # 'zbcd'
```

This script uses a list comprehension to filter out vowels from the input string, then uses the `join()` method to concatenate the remaining characters into a single string. The function is tested with the provided examples in the `if __name__ == "__main__":` block at the end.