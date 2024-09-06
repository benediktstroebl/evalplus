from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def parse_single_group(paren_str: str) -> int:
        if paren_str[0] != '(' or paren_str[-1] != ')':
            raise ValueError('Invalid input to the method. Parenthesis is not balanced.')
        depth = 0
        max_depth = 0
        for p in paren_str:
            if p == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            if p == ')':
                depth -= 1
                if depth < 0:
                    raise ValueError('Invalid input to the method. Parenthesis is not balanced.')
        return max_depth

    return [parse_single_group(paren_group) for paren_group in paren_string.split(' ')]

