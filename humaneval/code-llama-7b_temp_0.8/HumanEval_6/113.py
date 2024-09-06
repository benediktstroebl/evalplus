from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    """ALGORITHM"""
    # DEF. stack to store the number of open parens
    parens_stack = []
    # DEF. list to store the answer
    max_nested_parens = []
    # FOR. all characters in the paren_string
    for char in paren_string:
        # IF. the character is a left paren
        if char == '(':
            # THEN. push the stack and add one to the stack
            parens_stack.append(1)
        # ELIF. the character is a right paren
        elif char == ')':
            # THEN. pop from the stack and add one to the stack
            parens_stack.pop()
            # IF. the stack is empty
            if not parens_stack:
                # THEN. append 1 to the answer list
                max_nested_parens.append(1)
            # ELSE. append the pop value to the answer list
            else:
                max_nested_parens.append(parens_stack.pop() + 1)
        # ELSE. ignore other characters
    # RETURN the answer list
    return max_nested_parens

