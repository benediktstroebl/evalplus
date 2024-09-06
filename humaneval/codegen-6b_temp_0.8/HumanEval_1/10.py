from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Initialize empty list to store the split strings.
    split_strings = []
    index = 0
    # Loop while index is less than the length of the parenthesis string.
    while index < len(paren_string):
        # Store the index that the open paren starts at if we find one.
        open_index = index
        # While the index is less than the length of the parenthesis string and the character at the index is
        # an open parenthesis, add the open parenthesis to the open_index and increment the index.
        while index < len(paren_string) and paren_string[index] == '(':
            index += 1
        # Store the index that the close paren starts at if we find one.
        close_index = index - 1
        # While the index is less than the length of the parenthesis string and the character at the index is
        # a close parenthesis, add the open parenthesis to the open_index and increment the index.
        while index < len(paren_string) and paren_string[index] == ')':
            index += 1
        # If the index is not less than the length of the parenthesis string, decrement the index by 1.
        if index < len(paren_string):
            index -= 1
        # If the index is less than the length of the parenthesis string, check to see if the character after the
        # open paren is a close paren, which will indicate that this group is containing balanced parentheses.
        # If the character after the open paren is a close paren, add the group to the list of strings.
        # If the character after the open paren is an open paren, add the group to the list of strings and increment
        # the index.
        if index < len(paren_string) and paren_string[index + 1] == ')':
            split_strings.append(paren_string[open_index + 1:close_index + 1])
        else:
            split_strings.append(paren_string[open_index + 1:index])
    return split_strings


assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
assert separate_paren