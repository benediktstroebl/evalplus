from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse_parens_helper(stack: List[int], paren_string: str) -> List[int]:
        while paren_string:
            if paren_string[-1] == '(':
                stack.append(stack[-1] + 1)
            elif paren_string[-1] == ')':
                stack.append(stack[-1] - 1)
            paren_string = paren_string[:-1]
        return stack

    return [max(parse_parens_helper([0], paren_string)) for paren_string in paren_string.split()]
