

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Create a set of characters and their respective uppercase or lowercase versions
    character_map = {
        "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6",
        "7": "7", "8": "8", "9": "9", "A": "a", "B": "b", "C": "c", "D": "d",
        "E": "e", "F": "f", "G": "g", "H": "h", "I": "i", "J": "j", "K": "k",
        "L": "l", "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r",
        "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y",
        "Z": "z"
    }

    # Iterate through the string
    for char in string:
        # If the character is in the character_map, replace it with its uppercase or lowercase equivalent
        if char in character_map:
            string = string.replace(char, character_map[char])

    return string
