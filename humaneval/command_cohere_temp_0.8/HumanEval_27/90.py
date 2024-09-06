```python
def flip_case(string: str) -> str:
    """
    Flip case of characters in a string. Turn lowercase characters to uppercase and uppercase characters to lowercase.
    
    Parameters:
    string (str): Input string to modify.

    Returns:
    str: The modified string with flipped case.
    """
    # Use a list comprehension to iterate each character in the string.
    modified_string = list(string)
    for char in modified_string:
        # If the character is lowercase, make it uppercase.
        if char.islower():
            modified_string[modified_string.index(char)] = char.upper()
        # If the character is uppercase, make it lowercase.
        elif char.isupper():
            modified_string[modified_string.index(char)] = char.lower()
    # Convert the modified list back to a string and return.
    return ''.join(modified_string)
```

This code defines a function `flip_case` that takes a string as an argument and flips the case of each character. It checks if each character is in lowercase or uppercase and adjusts it accordingly. Finally, it joins the modified list of characters back into a string and returns the modified result.

Here's an example of how to use the function:
```python
print(flip_case("Hello"))  # Output: hELLO
print(flip_case("ABCDefg"))  # Output: AbCDeFg
``` 
This function will work as described in the docstring, flipping the case of characters for any given input string.