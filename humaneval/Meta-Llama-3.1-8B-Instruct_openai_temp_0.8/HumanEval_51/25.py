### Remove Vowels from a String
```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string from which vowels are to be removed.
    
    Returns:
    str: The input string without vowels.
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a generator expression to filter out vowels from the text
    # The join function is then used to convert the resulting generator back into a string
    return ''.join([char for char in text if char not in vowels])

# Test cases
if __name__ == "__main__":
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('abcdef') == 'bcdf'
    assert remove_vowels('aaaaa') == ''
    assert remove_vowels('aaBAA') == 'B'
    assert remove_vowels('zbcd') == 'zbcd'
    print("All test cases pass.")
```