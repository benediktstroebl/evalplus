from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def count_parentheses(string: str) -> int:
        count = 0
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def count_nesting(string: str) -> int:
        count = 0
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                count -= count
        return count

    # Check the length of the input string
    if len(paren_string) % 2 != 0:
        raise ValueError(f"Invalid input string: {paren_string}")

    return [count_nesting(part) for part in paren_string.split()]

