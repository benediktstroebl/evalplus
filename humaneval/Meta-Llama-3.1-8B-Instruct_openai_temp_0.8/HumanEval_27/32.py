```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with lowercase characters flipped to uppercase and uppercase to lowercase.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    result = ""
    for char in string:
        # Check if the character is an alphabet (uppercase or lowercase)
        if char.isalpha():
            # Use ASCII values to flip the case of the character
            if char.islower():
                result += chr(ord(char) - 32)
            else:
                result += chr(ord(char) + 32)
        else:
            # If the character is not an alphabet, just append it as it is
            result += char
    return result

print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```

This script defines the `flip_case` function that takes an input string, iterates over each character, checks if it's an alphabet, and flips its case using ASCII values. It also handles non-alphabet characters and returns the modified string. The example usage demonstrates the function's behavior with two different input strings.