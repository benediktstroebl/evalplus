from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    stack = []

    # Iterate over the s string
    for i in range(len(paren_string)):
        char = paren_string[i]

        # If we receive a right parenthesis
        if char == ')':
            # An empty stack means that we have an unbalanced left parenthesis
            if len(stack) == 0:
                return []

            # Peek at the top of the stack
            top_of_stack = stack.pop()

            if top_of_stack == '(':
                stack.append(2)
            else:
                nested_parens.append(len(stack) + 1)

        # If we receive a left parenthesis
        elif char == '(':
            stack.append(1)

    # After the end of the loop, we have the nested parens in the stack
    # Pop off all the left parens and return the value and number of parens in a list
    while len(stack) > 0:
        nested_parens.append(len(stack))
        stack.pop()

    return nested_parens

