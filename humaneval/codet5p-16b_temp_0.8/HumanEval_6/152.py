from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    result = []
    index = 0
    while index < len(paren_string):
        if paren_string[index] == '(':
            current_index = index
            depth = 0
            while depth < len(paren_string):
                if paren_string[depth] == '(':
                    depth += 1
                elif paren_string[depth] == ')':
                    if depth == current_index:
                        result.append(depth)
                        break
                    else:
                        depth -= 1
                        break
                else:
                    raise Exception("Invalid input")
        index += 1
    return result

