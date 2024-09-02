from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # keep track of the balanced nesting depth
    depth = 0
    # Keep track of the index in the input string where we want to start a new group
    start_idx = 0
    # Keep track of the index of the leftmost open brace in the current nesting group
    open_brace_idx = 0
    # Keep track of the index of the rightmost open brace in the current nesting group
    close_brace_idx = 0
    # Keep track of the groups that we've found
    groups = []
    for i, char in enumerate(paren_string):
        if char == "(":
            # If this is the first open brace we've found in this nesting group, record its index
            if depth == 0:
                open_brace_idx = i
            depth += 1
        elif char == ")":
            depth -= 1
            # If we're at the top nesting level and found a closing brace, it must be the last one in the nesting group
            if depth == 0:
                close_brace_idx = i
                # Add the current group to the list of groups
                groups.append(paren_string[start_idx:close_brace_idx + 1])
                # Reset the start index
                start_idx = i + 1
    return groups

