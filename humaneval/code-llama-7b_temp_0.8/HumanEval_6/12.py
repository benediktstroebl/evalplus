from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # 1. count the number of '(' and ')' and then return the deepest count by finding the max of both
    # 2. iterate through the string one character at a time
    # 3. if a '(' is found, increase the count by 1
    # 4. if a ')' is found, decrease the count by 1
    # 5. if the count is 0, return the max_count
    # 6. if the count is < 0, return -1
    max_count = 0
    count = 0
    for char in paren_string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        if count < 0:
            return -1
        if count > max_count:
            max_count = count

    if max_count == 0:
        return -1

    return max_count

