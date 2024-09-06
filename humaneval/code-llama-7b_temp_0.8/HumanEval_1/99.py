from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Initializing the list for groups
    groups = []
    # Nested function for handling recursion
    def separate_paren_groups_recursion(paren_string: str, i: int, groups: List[str]):
        # If we have reached the end of the string, return to the previous function
        if i == len(paren_string):
            return
        # Checking if we are at the beginning of a new group
        if paren_string[i] == "(":
            # Adding new group to the list
            groups.append("")
            # Calling the function recursively
            separate_paren_groups_recursion(paren_string, i + 1, groups)
        # Handling parentheses
        elif paren_string[i] == ")" and len(groups) > 0:
            # Removing the last character from the current group
            groups[-1] = groups[-1][:-1]
            # Calling the function recursively
            separate_paren_groups_recursion(paren_string, i + 1, groups)
        # Otherwise, add the current character to the current group
        else:
            groups[-1] += paren_string[i]
            # Calling the function recursively
            separate_paren_groups_recursion(paren_string, i + 1, groups)
    # Calling the function recursively
    separate_paren_groups_recursion(paren_string, 0, groups)
    # Returning the list
    return groups

