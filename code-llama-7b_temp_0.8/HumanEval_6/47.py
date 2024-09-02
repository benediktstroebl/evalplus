from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Getting rid of the whitespace in the string
    paren_string = paren_string.replace(" ", "")
    output: List[int] = []
    level = 0
    # Iterating over the string and updating the level based on open and close brackets
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            level += 1
        else:
            level -= 1
        output.append(level)
    return output

