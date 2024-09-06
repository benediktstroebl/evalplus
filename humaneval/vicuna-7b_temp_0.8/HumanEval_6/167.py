from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def count_opening_parens(s: str) -> int:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def count_close_parens(s: str) -> int:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def count_nested_parens(s: str) -> int:
        count = 0
        for char in s:
            if char == '(':
                count += 1
                while count > 0 and s[count] == '(':
                    count -= 1
            elif char == ')':
                count -= 1
        return count

    paren_string = paren_string.lower()
    paren_string = paren_string.replace(" ", "").replace("(", "").replace(")", "")

    # count opening parens
    nesting = 0
    for char in paren_string:
        if char == '(':
            nesting += 1
        elif char == ')':
            nesting -= 1
        else:
            nesting = max(nesting, count_opening_parens(paren_string[nesting:]))

    # count closing parens
    count_close_parens = lambda: count_close_parens(paren_string)
    count_close_parens(nesting)
    return [nesting] + list(map(count_close_parens, paren_string[nesting:].split('(')))