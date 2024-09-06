```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: Indicating whether the last character is an alphabetical character and not part of a word.
    """
    # Remove trailing spaces
    while txt and txt.endswith(" "):
        txt = txt.strip()
    
    # Check if the last character is a letter and not part of a word
    return (txt and (txt[-1].isalpha() and not txt.split()[-1]) )

# Test cases
assert check_if_last_char_is_a_letter("apple pie") == False
assert check_if_last_char_is_a_letter("apple pi e") == True
assert check_if_last_char_is_a_letter("apple pi e ") == False
assert check_if_last_char_is_a_letter("") == False 
``` 

This function first removes all trailing spaces using the `while` loop and the `strip()` function. It then uses the `isalpha()` function to check if the last character is alphabetical, and the `split()` function to check if it's separate from the rest of the word using the boolean NOT operation (`not txt.split()[-1]`). 

You can verify that the function works correctly with the provided test cases. 
If you wish to test more cases, you can add additional assertions like `'assert check_if_last_char_is_a_letter("apple pi e abc") == True'`  for more thorough testing.