```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to flip case.
    
    Returns:
        str: The string with case flipped.
    """
    result = ""
    for char in string:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            # If the character is neither uppercase nor lowercase (e.g. a punctuation mark), leave it as is
            result += char
    return result

# Example usage
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wORLD'
print(flip_case('hello WORLD'))  # Output: 'HELLO wORLD'
```