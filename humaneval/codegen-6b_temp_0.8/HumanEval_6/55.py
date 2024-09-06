from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    lst = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            num_left = 1
            for j in range(i + 1, len(paren_string)):
                if paren_string[j] == "(":
                    num_left += 1
                elif paren_string[j] == ")":
                    num_left -= 1
                if num_left == 0:
                    lst.append(j - i)
                    break
        i += 1
    return lst

