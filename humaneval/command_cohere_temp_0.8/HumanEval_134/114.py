```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string into words based on spaces
    words = txt.split()
    final_char = words[-1][-1] if len(words) > 0 else None
    
    return final_char is not None and final_char.isalpha() and not final_char.isalpha().isalnum()
```

The function leverages the `split()` method to divide the input string into an array of words, wherein the last character of the string is extracted and checked using the `isalpha()` method. Additionally, the `isalnum()` method is employed to ensure the last character is not part of a word, ultimately returning `True` if the aforementioned conditions are met. 

This approach allows the function to effectively determine whether the last character of the input string is an alphabetical character distinct from any word boundaries, ultimately returning `True` in such cases and `False` otherwise. Feel free to experiment with different scenarios to adequately understand the functionality of the function.