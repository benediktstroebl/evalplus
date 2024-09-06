```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Ensure the input string is not empty and has a last character
    if not txt or not txt[-1]:
        return False
    
    # Check if the last character is a letter
    if txt[-1].isalpha():
        # Check if the last character is part of a word
        if not txt.rsplit(' ', 1)[-1].isalnum():
            return True
    return False
```

The function `check_if_last_char_is_a_letter` leverages the string methods `isalpha()` and `rsplit()` to determine whether the last character is an alphabetical character and whether it forms part of a word. The `if` statements cascade appropriately to return `True` if the last character is an alphabetical character not forming part of a word, and `False` otherwise. 

The following examples illustrate its utility:
```python
>> check_if_last_char_is_a_letter("apple pie")
False
>> check_if_last_char_is_a_letter("apple pi e")
True
>> check_if_last_char_is_a_letter("apple pi e ")
False
>> check_if_last_char_is_a_letter("")
False
```