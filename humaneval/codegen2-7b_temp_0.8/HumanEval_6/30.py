from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level = 0
    current_paren = 0
    output = []
    for idx, ch in enumerate(paren_string):
        if ch == '(':
            level += 1
            if level > current_paren:
                current_paren = level
                output.append(current_paren)
        elif ch == ')':
            level -= 1
            if level < current_paren:
                current_paren = level
                output.append(current_paren)
    
