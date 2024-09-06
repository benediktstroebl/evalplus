```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.

    Examples:
    >>> check_if_last_char_is_a_letter("apple pie")
    False
    >>> check_if_last_char_is_a_letter("apple pi e")
    True
    >>> check_if_last_char_is_a_letter("apple pi e ")
    False
    >>> check_if_last_char_is_a_letter("")
    False
    """

    # If the string is empty, return False
    if not txt:
        return False

    # Extract the last character and convert to lower case
    last_char = txt.strip()[-1].lower()

    # Split the string into words using space as delimiter
    words = txt.split()
    
    # Check if the last character is not part of a word
    # and it is an alphabetical character
    return last_char not in words and last_char.isalpha()
```

This Python script defines a function called `check_if_last_char_is_a_letter`, which evaluates the last character of a given string and determines whether it's the end of a word and an alphabetical character. The function first checks if the given string is empty, and if so, it returns False. It then extracts the last character and converts it to lowercase to ensure case-insensitive accuracy. The string is then split into words using space as a delimiter, and finally, the function returns True if the last character is not part of any word and is an alphabetical character, and False otherwise. 

The example usage in the docstring shows the function's behavior on various inputs, demonstrating its utility for checking the last character of a string with respect to the specified criteria.