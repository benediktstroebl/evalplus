from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Replace all instances of multiple consecutive whitespace with a single space
    clean_str = re.sub(r'\s+','', paren_string)

    # Get indices of all the open and close parentheses
    open_paren_indices = [
        i for i, char in enumerate(clean_str) if char == "("
    ]
    close_paren_indices = [
        i for i, char in enumerate(clean_str) if char == ")"
    ]

    # Check if the parentheses are balanced
    if len(open_paren_indices)!= len(close_paren_indices):
        raise ValueError("Parentheses are not balanced")

    # Build the list of tuples of parentheses
    groups = []
    for i in range(len(open_paren_indices)):
        groups.append(
            (
                open_paren_indices[i],
                close_paren_indices[i]
            )
        )

    # Return the list of parentheses
    return [
        clean_str[group[0]:group[1] + 1]
        for group in groups
    ]
