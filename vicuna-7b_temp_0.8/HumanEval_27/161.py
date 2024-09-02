

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Convert the input string to a list of characters
    chars = string.split()
    # Iterate over the list of characters
    for i, c in enumerate(chars):
        # If the character is a lowercase letter, flip it to uppercase
        if c.islower():
            chars[i] = chr(ord(c) - ord('A') + ord('B'))
    # Join the characters back into a string
    return ''.join(chars)
