from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # TODO
    # Start thinking about how to do it and
    # try to implement it by yourself!
    # Hint: what happens when you put an opening parenthesis into a string?

    # Empty String
    if not paren_string:
        return []

    # Split into smaller strings and ignore white spaces
    smaller_strings = paren_string.split(" ")

    # Empty string can't be a valid string
    if len(smaller_strings) == 0:
        return []

    # Reverse the string for easier implementation
    smaller_strings.reverse()

    # Create an empty list
    result = []

    # Loop through each string until the list is empty
    while len(smaller_strings) > 0:
        # Put the first string into a new list
        first_string = smaller_strings.pop()

        # Check if the string starts with '('
        if first_string.startswith("("):
            # Append to result
            result.append(first_string)

            # Append to result
            result
