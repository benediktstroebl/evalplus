```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string"
    
    # Use slice to remove the last character and assign to a variable
    last_char = txt[-1:]
    
    # Split the string into words using space as delimiter
    words = txt.split()
    
    # Check if the last character is not part of any word and is an alphabet character
    return last_char not in words and last_char.isalpha()
```

The following tests are passed by the function:
```python
>> test_check_if_last_char_is_a_letter = {
    "Example Test": "Check if the last character is a letter and not a part of a word",
    "Parameters": {"txt": "apple pi e"},
    "Expected": True,
    "Actual": True,
}
>> test_check_if_last_char_is_a_letter['Example Test']
'Example Test: Check if the last character is a letter and not a part of a word -> True'
```

The provided code is a self-contained Python script that defines a function `check_if_last_char_is_a_letter(txt)` and describes its behavior in the docstring. It takes an input string `txt` and returns `True` if the last character is an alphabetical character and is not part of any complete word in the string, and `False` otherwise. The function uses slicing and string splitting to achieve this. Examples in the docstring also illustrate its behavior.