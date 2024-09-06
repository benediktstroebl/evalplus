from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # We use a stack to keep a track of the current nesting level
    stack = []
    max_nesting_level = 0

    # We iterate through the string and find the level of nesting
    for i in range(len(paren_string)):

        # With this if condition to prevent the index out of bounds error
        if i >= len(paren_string):
            break

        # We check if it is an open parenthesis
        if paren_string[i] == '(':
            stack.append('(')
            max_nesting_level += 1

        # If it is a closing parenthesis, we also check if the stack is not empty
        elif paren_string[i] == ')':
            # If the stack is empty, return -1
            if not stack:
                return -1

            # If the stack is not empty, we pop the stack and check if it's a matching pair of parentheses
            # If we find a pair of parentheses, we increase the nesting level
            # If the pair of parentheses is not matched, we return -1
            else:
                stack.pop()
                max_nesting_level = max(max_nesting_level, len(stack))

    # final result is the max_nesting_level if the string is balanced, -1 otherwise
    if max_nesting_level == len(stack):
        return max_nesting_level
    else:
        return -1

