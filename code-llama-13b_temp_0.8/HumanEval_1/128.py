from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # 1. iterate over the input string
    # 2. find the first occurence of '('
    # 3. keep track of the current_level of nested parentheses
    # 4. when you reach a '(' at a level > 0, increase the current_level
    # 5. when you reach a ')' at a level > 0, decrease the current_level
    # 6. when you reach a ')' at level 0, close the current group and start a new one
    # 7. when you finish iterating the input string, return the list of current groups
    level = 0
    current_group = []
    current_paren_group = []
    paren_groups = []
    for paren in paren_string:
        if paren == '(':
            level += 1
        if paren == ')' and level == 0:
            raise ValueError("Unbalanced parantheses!")
        if paren == ')':
            level -= 1
        if paren != ' ':
            current_paren_group.append(paren)

        if current_paren_group and level == 0:
            paren_groups.append(''.join(current_paren_group))
            current_paren_group = []

    return paren_groups

