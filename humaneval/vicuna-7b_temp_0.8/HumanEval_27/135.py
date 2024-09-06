

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # O(n) space and time complexity
    reversed_string = string[::-1]
    # O(n) time complexity
    for char in reversed_string:
        if char.islower():
            char = chr(ord(char) - ord('A') + 'A')  # O(1)
        elif char.isupper():
            char = chr(ord(char) - ord('a') + 'a')
    return reversed_string
