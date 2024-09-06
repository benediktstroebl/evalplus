from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Cases:
    # 1. The string is empty
    # 2. There is a pair of brackets inside a string
    # 3. There are no brackets in a string
    # 4. There is a bracket at the end of a string
    # 5. There is a bracket at the beginning of a string

    # 1.
    if paren_string == '':
        return []

    # 2.
    if paren_string.count('(') == 0:
        return []

    # 3.
    if '(' not in paren_string:
        return [paren_string]

    # 4.
    if paren_string[0] == '(':
        return [paren_string]

    # 5.
    if paren_string[-1] == ')':
        return [paren_string]

    # Indices of all '(' characters
    start_indices = [i for i, x in enumerate(paren_string) if x == '(']

    # Indices of all ')' characters
    end_indices = [i for i, x in enumerate(paren_string) if x == ')']

    # 1.
    if len(start_indices) == 0:
        return [paren_string]

    # 2.
    if len(start_indices) == len(end_indices):
        return [paren_string]

    # 3.
    if len(start_indices) < len(end_indices):
        return [paren_string]

    # 4.
    if len(start_indices) > len(end_indices):
        return [paren_string]

    # 5.
    # Checking if the string is balanced
    if start_indices[0] > 0:
        return [paren_string[:start_indices[0]].strip()] + separate_paren_groups(paren_string[start_indices[0]:])

    # 6.
    # Removing all the starting and ending brackets
    
