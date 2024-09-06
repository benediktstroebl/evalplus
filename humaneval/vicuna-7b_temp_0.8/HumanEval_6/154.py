from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    return_value = [0] * len(paren_string)
    # Inside loop starts from 1 as 0 is used as special marker for the last element
    for i in range(1, len(paren_string)):
        level = 0
        start = i
        for j in range(1, len(paren_string)):
            if paren_string[j] == '(':
                level += 1
            elif paren_string[j] == ')':
                level -= 1
            # Check for the next closing parenthesis
            if level == 0 and paren_string[j] == ')':
                break
            elif paren_string[j] == ' ':
                start = j
            elif paren_string[j] == ')':
                start = j
        # Replace the starting index with the end index + 1
        return_value[start] = return_value[start] + 1
    return return_value