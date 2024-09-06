from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # -------------------- INITIALIZE VARIABLES --------------------
    stack: List[int] = []  # Will be used as a stack, to count the number of open parentheses
    max_nesting: List[int] = []  # Will be the output list of deepest level of nesting

    # -------------------- ITERATE OVER STRING --------------------
    for i, paren in enumerate(paren_string):
        # If paren is open, push the number of parentheses seen so far on to the stack
        if paren == "(":
            stack.append(i + 1)
        # If paren is close, pop the top value from stack
        # to check the number of open parentheses when this one was opened
        elif paren == ")":
            max_nesting.append(stack.pop())
        # If neither, ignore
        else:
            pass

    # -------------------- RETURN THE OUTPUT --------------------
    return max_nesting

