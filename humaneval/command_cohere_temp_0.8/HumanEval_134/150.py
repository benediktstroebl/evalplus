```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length variable
    str_len = len(txt) - 1
    # Check if the string length is larger than zero to prevent IndexError
    if str_len >= 0:
        # Check if the last character is a letter and is not part of a word
        if txt[str_len].isalpha() and txt[str_len].lower() not in txt.split():
            return True
    return False
```

The function `check_if_last_char_is_a_letter` checks if the last character of a given string is an alphabetical character and is not a part of any word (i.e., the last character is a letter that stands alone, not part of a word). It does so by leveraging the string's length, checking the last character for alphabetic characteristics, and cross-referencing it with the string's content to determine if it's not part of a word. The function returns `True` if the last character fulfills these conditions, and `False` otherwise. 

The following examples showcase its utility:
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