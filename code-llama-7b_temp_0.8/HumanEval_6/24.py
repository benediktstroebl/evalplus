from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Initialize a stack that will keep track of indices
    # of opening parentheses.
    open_parentheses = [-1]  # -1 is a dummy value for the 0th index
    max_level = 1  # Initialize the maximum level to 1
    depth_of_nesting = []  # Store the depth of nesting for each group

    for index, paren in enumerate(paren_string):

        # If this is an opening parenthesis, append its index to the stack
        # and increase the maximum level if it is greater than the current max.
        if paren == '(':
            open_parentheses.append(index)
            max_level = max(max_level, len(open_parentheses) - 1)

        # If this is a closing parenthesis, pop the stack.
        elif paren == ')':
            open_parentheses.pop()

        # If we have reached the end of the string, calculate the depth of nesting
        # for all groups (up to the maximum level of nesting) and store them in a list.
        if index == len(paren_string) - 1:
            for level in range(max_level):
                depth_of_nesting.append(level + 1)

    return depth_of_nesting

