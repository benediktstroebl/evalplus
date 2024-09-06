```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Trim any whitespace from the end of the string
    txt = txt.strip()

    # Check if the string ends with a space
    if txt.endswith(" "):
        return False

    # Check if the last character is a letter and not part of a word
    # By using both lowercase and uppercase 'A' as a proxy to represent alphabetical characters
    if txt[-1].lower() in 'abcdefghijklmnopqrstuvwxyz' and txt[-1].upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return not txt.split(" ")[-1]
    else:
        return False
```

The function `check_if_last_char_is_a_letter` determines whether the final character of a given string is an alphabetical character and is not a component of a word. It accomplishes this by first using the `endswith` method to verify if the string ends with a space, effectively excluding situations where the examination criterion is a part of a word. Next, it examines the penultimate character to determine if it is an alphabetical character and is not part of a word. To do this, it uses both lowercase and uppercase 'A' as a stand-in to represent all alphabetical characters. If the penultimate character fulfills these requirements, the function returns `True`; otherwise, it returns `False`. 

This approach ensures that the function appropriately detects if the last character is an alphabetical character without considering it part of a word.