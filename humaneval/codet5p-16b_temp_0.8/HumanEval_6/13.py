from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    output: List[int] = []
    paren_list = paren_string.split()
    for i in paren_list:
        counter = 0
        for j in i:
            if j == '(':
                counter += 1
            if j == ')':
                counter -= 1
                if counter < 0:
                    counter = 0
                    break
        output.append(counter)
    return output

