from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # The current string that we are working on
    current_string = paren_string

    # Keep track of the open braces
    open_brace_count = 0

    # Keep track of the nested groups
    nested_groups = []

    # Keep track of the last opened brace
    last_opened_brace = None

    # Iterate through the string
    for c in current_string:
        # If we are closing a brace, reset the last opened brace
        if c == '}':
            last_opened_brace = None

        # If we are opening a brace, we start a new group
        elif c == '(':
            open_brace_count += 1

        # If we are closing a brace and it is not the last one, add it to the nested_groups list
        elif c == '}' and last_opened_brace is not None:
            nested_groups.append(current_string[last_opened_brace + 1:])

            # Reset the last opened brace
            last_opened_brace = None

        # If we are closing the last brace, return the list of nested groups
        elif c == '}' and open_brace_count == 0:
            nested_groups.append(current_string)
            break

    # If there are any remaining open braces, add them to the last nested group
    if last_opened_brace is not None:
        nested_groups.append(current_string[last_opened_brace + 1:])

    return nested_groups
 ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇ 
