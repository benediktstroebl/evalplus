from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parsed_string = ""
    parsed_characters = []
    for character in paren_string:
        if character == ")":
            parsed_characters.append(character)
            last_char = parsed_characters[-1]
            if last_char == "(":
                parsed_characters.pop()
                parsed_characters.pop()
                parsed_string += "".join(parsed_characters)
                parsed_characters = []
            else:
                break
        elif character == "(":
            parsed_characters.append(character)
            last_char = parsed_characters[-1]
            if last_char == "(":
                parsed_characters.pop()
                parsed_characters.pop()
                parsed_string += "".join(parsed_characters)
                parsed_characters = []
            else:
                break
        else:
            parsed_characters.append(character)
    if parsed_characters:
        parsed_string += "".join(parsed_characters)
    return parsed_string.split(" ")

