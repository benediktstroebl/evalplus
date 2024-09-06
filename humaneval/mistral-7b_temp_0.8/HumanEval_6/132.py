from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # TODO: implement me
    # Hint: You'll want to convert the string to a list.

    if len(paren_string) == 0:
        return []

    parentheses = list(paren_string)
    open_parens = []
    close_parens = []
    stack = []
    levels = []

    for parenthesis in parentheses:
        if parenthesis == "(":
            open_parens.append(parenthesis)
        elif parenthesis == ")":
            if not len(open_parens):
                return []
            close_parens.append(parenthesis)
            stack.append(open_parens.pop())
        else:
            return []

    while len(open_parens):
        stack.append(open_parens.pop())

    for open_paren, close_paren in zip(stack, close_parens[::-1]):
        if open_paren == close_paren:
            levels.append(1)
        else:
            levels.append(2)

    return
