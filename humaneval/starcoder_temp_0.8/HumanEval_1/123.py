from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # 1. remove spaces
    paren_string = paren_string.replace(" ", "")
    # 2. initialize stack
    stack = list()
    # 3. iterate over characters in the input string
    for char in paren_string:
        # 4. if character is (, add to stack
        if char == "(":
            stack.append(char)
        # 5. if character is ), pop stack
        elif char == ")":
            stack.pop()
    # 6. add groups to list
    groups = list()
    for char in paren_string:
        # 7. if char is (, start a group
        if char == "(":
            group = ""
            # 8. while stack is not empty, add to the group
            while stack:
                group += stack.pop()
            # 9. add to list
            groups.append(group)
    # 10. return list of groups
    return groups

