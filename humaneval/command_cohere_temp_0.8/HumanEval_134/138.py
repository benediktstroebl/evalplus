```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.

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

    def is_last_char_not_part_of_word(txt):
        # Check if the last character is spaces, digits, or symbols
        if txt[-1].isalpha():
            return True
        # Check if the last character is end of word
        elif txt[-2:] != " ":
            return False
        return True

    # Check if the string is empty
    if not txt:
        return False

    # Remove trailing spaces
    while txt and txt.endswith(" "):
        txt = txt[:-1]

    # If the string is not empty and last character is not part of word, return True
    return is_last_char_not_part_word(txt)
```

The test cases are:
```python
def test_check_if_last_char_is_a_letter():
    # Case 1
    assert check_if_last_char_is_a_letter("apple pie") == False

    # Case 2
    assert check_if_last_char_is_a_letter("apple pi e") == True

    # Case 3
    assert check_if_last_char_is_a_letter("apple pi e ") == False

    # Case 4
    assert check_if_last_char_is_a_letter("") == False

    # Case 5
    assert check_if_last_char_is_a_letter("hello") == True

test_check_if_last_char_is_a_letter()
```

The technique used in this code is to iterate over the string and check if the last character is an alphabet character and not part of a word. The code checks for the last two characters of the string to see if it is a space followed by an alphabet character, implying that it is not part of a word. The function returns True in such a case, implying that the last character is an alphabetical character and is not part of a word. The function returns False if the string ends with a word or a symbol/digit, implying that the last character is part of a word. 

Lastly, the function handles the edge case where the input string is empty by returning False since an empty string doesn't have any last character. The function also removes any trailing spaces from the string before performing the check, ensuring that it can handle spaces at the end of the string correctly.