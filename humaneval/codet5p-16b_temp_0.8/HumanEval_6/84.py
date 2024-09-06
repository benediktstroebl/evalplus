from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens_stack: List[int] = []
    results: List[int] = []

    for idx, char in enumerate(paren_string):
        if char == '(':
            parens_stack.append(idx)
        elif char == ')':
            if parens_stack:
                results.append(parens_stack.pop())
            else:
                raise Exception(f"Invalid string: Empty stack at index {idx}.")

    return results

