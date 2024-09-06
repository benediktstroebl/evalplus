from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Loop through the string and keep track of the current level of nesting as we encounter the opening parentheses
    current_nesting = 0
    max_nesting = 0
    output = []
    for paren in paren_string:
        if paren == '(':
            current_nesting += 1
        elif paren == ')':
            current_nesting -= 1

        # Keep track of the maximum number of parentheses we have seen so far
        if current_nesting > max_nesting:
            max_nesting = current_nesting

        # When we reach the end of the group, append the result to the output
        if paren == ')':
            output.append(max_nesting)
            max_nesting = 0

    return output

