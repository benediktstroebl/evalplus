```python
def check_if_last_char_is_a_letter(txt):
    '''
    Checks if the last character of a string is an alphabetical 
    character and is not part of a word.

    Parameters:
    txt (str): Input string.

    Returns:
    bool: True if the last char is an alphabetical character 
    and is not part of a word, False otherwise.
    '''
    words = txt.split()
    last_char = txt[-1]

    if len(words) == 0:
        return False

    if len(words) == 1:
        return txt[-1].isalpha()

    return words[-1][-1].isalpha()
```