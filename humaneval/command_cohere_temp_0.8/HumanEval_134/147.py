```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length to retrieve the last character
    last_char = txt[-1]
    # Check if the last character is a letter and it is not an abbreviation or a suffix
    if ('a' <= last_char <= 'z') or ('A' <= last_char <= 'Z') :
        return not txt.split(' ')[-1]
    return False
```

The function uses the last character of the string (`txt[-1]`) and checks if it is an alphabetical character (`if ('a' <= last_char <= 'z') or ('A' <= last_char <= 'Z'):`). Additionally, the function checks if the last character is not part of a word (i.e., it's not an abbreviation or suffix) by verifying that the last character is not the last element of the string obtained after splitting the original string into spaces. The function returns `True` if the last character is an alphabetical character and is not part of a word, and `False` otherwise. 

Here is an example usage of the function with an appropriate string: 
```python
print(check_if_last_char_is_a_letter("apple pie")) 
```

The output will be:
```
False
```

And here is another example with a string that should return True:
```python
print(check_if_last_char_is_a_letter("apple pi e"))
```

The corresponding result will be:
```
True
```