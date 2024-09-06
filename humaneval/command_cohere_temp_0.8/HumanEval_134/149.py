```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define a regular expression pattern to match alphabetic characters
    alpha_pattern = r'[a-zA-Z]'

    # Check if the string is empty
    if not txt:
        return False

    # Find the last character in the string
    last_char = txt[-1]

    # Check if the last character is alphabetic
    if re.search(alpha_pattern, last_char):
        # Check if the last character is separated from the previous word
        return not re.search(r'([\w]+)' + alpha_pattern, txt)

    return False
```

The function uses the `re` module's search function to check if the last character of the string txt matches the pattern [a-zA-Z] which corresponds to alphabetical characters. It also uses the same module's search function with the regular expression pattern ([\w]+)alpha_pattern to check if the last character is separated from the previous word. The function returns True if the last character is an alphabetical character and is not part of a word, and False otherwise. It also handles the edge case where the input string is empty by returning False. 

The expected behavior is shown in the following examples:
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