from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def helper(paren_string: str) -> int:
        """
        Time Complexity: O(n), n = len(paren_string)
        Space Complexity: O(1)
        """
        if len(paren_string) == 0:
            return 0

        stack: List[str] = []
        max_level = 0

        for paren in paren_string:
            if paren == '(':
                stack.append(paren)
            elif paren == ')':
                if len(stack) != 0:
                    stack.pop()
                    max_level = max(max_level, len(stack))
                else:
                    return 0

        return max_level

    return list(map(helper, paren_string.split(' ')))

