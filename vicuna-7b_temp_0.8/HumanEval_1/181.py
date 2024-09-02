from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Create a string builder to build the output string
    output = ""

    # Iterate through each character in the input string
    for char in paren_string:
        # If the character is an open brace, append it to the output string
        if char == "(":
            output += char

        # If the character is a close brace, check if the previous character is an open brace
        # If it is, the group of parentheses is not properly balanced and we should ignore it
        elif char == ")" and output.endswith("("):
            output = output[:-1]  # Remove the extra open brace from the output
            continue

        # If the character is a close brace, we have a balanced group of parentheses, so add it to the output
        # If it is the first character of the group, start a new output string
        elif char == ")" and not output.endswith("("):
            output += char
            if output.endswith(")"):
                # This is the last character of the group and the output string is not empty, so return it
                return [output]

        # If the character is any other character, append it to the output string
        else:
            output += char

    # If we get here, the input string is empty or contains only one unbalanced parenthesis, so return an empty list
    return []

