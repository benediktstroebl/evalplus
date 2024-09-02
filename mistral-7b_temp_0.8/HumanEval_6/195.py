from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # "Parse" nested parentheses into a list of parentheses with nested levels
    stack = []
    parentheses_with_levels = []
    for paren in paren_string.strip().split():
        if paren == '(':
            stack.append(1)
        elif paren == ')':
            stack.pop()
        else:
            raise ValueError(f"Expected '(' or ')' not '{paren}'")
        if stack:
            parentheses_with_levels.append((paren, max(stack)))

    # Return the highest level of nesting in the list of parentheses
    return [p[1] for p in parentheses_with_levels]

