from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # # One line solution
    # return re.findall('\(([^()]*)\)', paren_string)

    # Initializing a list that will store the separated strings
    separated_paren_groups = []

    # Initializing a string that will store the current nested group
    current_nested_group = ''

    # Initializing a flag that will keep track of whether we are inside a nested group
    inside_nested_group = False

    # Iterating through the characters in the input string
    for character in paren_string:

        # If we encounter an open parenthesis, then we start adding characters to the current group
        if character == '(':
            inside_nested_group = True

        # If we encounter a close parenthesis, then we are done adding characters to the current group
        if character == ')':
            inside_nested_group = False
            separated_paren_groups.append(current_nested_group)
            current_nested_group = ''

        # If we are inside a nested group, then we add the character to the current group
        if inside_nested_group:
            current_nested_group += character

    return separated_paren_groups

