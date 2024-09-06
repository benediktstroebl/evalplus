from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # The algorithm for separating groups into separate strings is to keep a stack of open parentheses
    # as we go through the string. As soon as we see a close parenthesis, we pop the top element from
    # the stack. As we go, we keep building up the string until we finish the group. So, once we pop
    # the last open brace, we add the string we've built so far to the list of results.
    # The algorithm is O(n) because we're going through the string once.
    open_parens_stack = []
    groups = []
    current_group = ""

    for char in paren_string:
        if char == "(":
            open_parens_stack.append("(")
        elif char == ")":
            # If there are no more open parens left in the stack, we've finished the group.
            if len(open_parens_stack) == 0:
                groups.append(current_group)
                current_group = ""
            else:
                # We've finished the group. So, we pop an open paren from the stack and append
                # the current group to the list of results.
                open_parens_stack.pop()
                groups.append(current_group)
                current_group = ""
        else:
            # We're not seeing a brace so we add that to the group
            current_group += char

    if len(open_parens_stack) > 0:
        raise ValueError(
            "There are more open parentheses than close parentheses in the input string"
        )

    return groups

