from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Convert the input string to a set of parentheses.
    parenthesis_set = set(paren_string)
    # Create an empty list to store the result.
    result = []
    # For each element in the set of parentheses
    for element in parenthesis_set:
        # If it's not a parenthesis, it's an opening brace, so add it to the result.
        if element not in '()':
            result.append(element)
        # If it's a closing brace, find the next opening brace and add it to the result.
        elif element == '(':
            next_brace = parenthesis_set.index(element) + 1
            while next_brace < len(parenthesis_set) and parenthesis_set[next_brace] == '(':
                next_brace += 1
            result.append(parenthesis_set[next_brace])
    return result

