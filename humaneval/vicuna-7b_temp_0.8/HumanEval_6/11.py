from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = [0] * 2 # initialize a list of zeros with length 2 (to store the count for each level of nesting)

    def helper(s):
        # Helper function to extract the count for the current level of nesting
        for char in s:
            if char == '(':
                count[0] += 1
            elif char == ')':
                count[1] += 1
                if count[0] > 0 and count[1] > 0:
                    break
    # Recursive function to traverse through the string and extract the count
    helper(paren_string)
    return count

