from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_level = 0
    stack = []
    parens = [i for i, c in enumerate(paren_string) if c == '(']
    index, max_nested = 0, 0
    for j, paren in enumerate(parens):
        if paren > index:
            stack.append(paren)
            index = paren
        else:
            temp = 0
            while stack and (stack[-1] > index):
                temp += 1
                stack.pop()
                index = stack[-1]
            max_nested = max(max_nested, temp)
    return [max_nested] * len(parens)

