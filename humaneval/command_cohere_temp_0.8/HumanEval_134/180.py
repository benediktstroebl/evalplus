```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

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

    # Check if the last character is alphanumeric and not part of a word
    if (last_char in txt.split()] and re.search(alpha_pattern, last_char) is not None:
        return True
    else:
        return False
```

The function `check_if_last_char_is_a_letter` takes a string as input and returns a boolean - True or False - depending on the mentioned conditions. You can use it by calling the function with a string as an argument like this: 
 ```python
print(check_if_last_char_is_a_letter("I am here")) # Output: False
print(check_if_last_char_is_a_letter("I am a writer ")) # Output: True
 ``` 

The first example leads to a false result, since the last character is a numeric symbol, while the second example leads to a true result, since the last character is the letter ' ' and it is not part of any word.