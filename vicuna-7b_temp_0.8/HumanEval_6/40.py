from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def count_depth(s: str, depth: int = 0) -> int:
        """
        Recursive function to count the number of open parentheses in a string s
        at a given depth level.

        Parameters:
            s (str): The string to count the number of open parentheses.
            depth (int): The current depth level.

        Returns:
            int: The number of open parentheses in the string s at the given depth level.
        """
        for char in s:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
                if depth == 0:
                    return -1
        return depth

    def count_groups(s: str) -> int:
        """
        Recursive function to count the number of groups of nested parentheses in a string s.

        Parameters:
            s (str): The string to count the number of groups of nested parentheses.

        Returns:
            int: The number of groups of nested parentheses in the string s.
        """
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count == 0:
                    return -1
        return count

    def count_parens(s: str) -> int:
        """
        Recursive function to count the number of open parentheses in a string s.

        Parameters:
            s (str): The string to count the number of open parentheses.

        Returns:
            int: The number of open parentheses in the string s.
        """
        return s.count('(')

    def get_max_nesting(s: str) -> int:
        """
        Recursive function to get the maximum nesting of parentheses in a string s.

        Parameters:
            s (str): The string to get the maximum nesting of parentheses.

        Returns:
            int: The maximum nesting of parentheses in the string s.
        """
        if s == '':
            return 0
        elif s == ')':
            return 1
        else:
            max_nesting =
