```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string.
    
    Returns:
    str: The string with case flipped.
    
    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ""
    for char in string:
        # Check if character is a letter
        if char.isalpha():
            # If letter, convert it to the opposite case
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            # If not a letter, add it as is
            result += char
    return result

# Test the function
print(flip_case('Hello'))  # Outputs: hELLO
print(flip_case('Hello, World!'))  # Outputs: hELLO, wORLD!
```

This Python script defines a `flip_case` function that takes a string as input, flips the case of each letter in the string, and returns the resulting string. The function iterates over each character in the input string. If the character is a letter, it converts it to the opposite case; if the character is not a letter, it adds it to the result as is. The script also includes test cases to demonstrate the function's behavior.