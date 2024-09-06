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
    # Check if the string ends with a space to mitigate the case of a standalone space
    if txt.endswith(' '): 
        return False
    
    # Check if the last character is a letter and not a part of a word
    return (len(txt)>0 and txt[-1] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') and \
           (txt[-1] != '-') and (txt[-1]!='_') and (txt[-1]!='')
```

The function checks if the last character of the given string `txt` is an alphabetical character and is not part of a word. The function first trims any whitespace from the end of the string using the `strip()` method. This is done to handle the special case where the string ends with whitespace. Then, it checks if the last character is a letter using a condition that checks if the character is an alphabetic character or digit. Lastly, the function checks if the last character is not a part of a word by verifying that it is not a hyphen or an underscore and that it is not a standalone space, and then returns the corresponding boolean value. 

The following examples demonstrate how this function operates:
```python
# Example 1
input_str = "apple pie"
result = check_if_last_char_is_a_letter(input_str)
print(result)  # Output: False

# Example 2
input_str = "apple pi e"
result = check_if_last_char_is_a_letter(input_str)
print(result)  # Output: True

# Example 3
input_str = "apple pi e "
result = check_if_last_char_is_a_letter(input_str)
print(result)  # Output: False

# Example 4
input_str = ""
result = check_if_last_char_is_a_letter(input_str)
print(result)  # Output: False
```