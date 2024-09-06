from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    opening = ["(", "[", "{", "<"]
    closing = [")", "]", "}", ">"]

    open_count = 0
    closed_count = 0
    level = 0
    nested_parens = []
    for token in paren_string:
        if token in opening:
            open_count += 1
            level = max(open_count, level)
        elif token in closing:
            closed_count += 1
            level = max(open_count - closed_count, level)
        if token == ")":
            # a hack to ensure that the next token is not ")"
            # instead, it is a space or the end of the string
            if paren_string[1:].startswith(")("):
                paren_string = paren_string.replace(")(", "")
            else:
                break
    nested_parens.append(level)
    return nested_parens
