from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Create list of list in order to represent stack
    stack = [[] for _ in range(len(paren_string))]
    # Keep track of level count in stack as we iterate through paren_string
    level_count = 0
    # Iterate through string
    for i, paren in enumerate(paren_string):
        if paren == '(':
            level_count += 1
            stack[i].append('(')
        elif paren == ')':
            level_count -= 1
            if level_count < 0:
                return None
            stack[i].append(')')
    # If we don't hit the end of the string then we have an uneven number of (
    if level_count != 0:
        return None
    # If we reach the end of the string then we've gone through the last )
    else:
        # Get length of each list in the stack
        lengths = [len(lst) for lst in stack]
        # If there exists 3 or more empty lists in stack
        if sum(lengths) == len(lengths):
            return None
        # Otherwise there is a nesting level
        else:
            return lengths.index(max(lengths))

