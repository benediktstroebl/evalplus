from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # First we count the number of left parens.
    left_parens_count = paren_string.count("(")

    # Then, we count the number of right parens to get the number of closing parentheses we need to match.
    right_parens_count = paren_string.count(")")

    # Then, we split the string at each space to get a list of string elements.
    paren_string_list = paren_string.split(" ")

    # Finally, we create a stack (i.e. a list) to keep track of the parentheses we match.
    stack = []

    # Finally, we start looping through the list.
    for paren_string in paren_string_list:
        # If we are at a left parentheses, we push it to the stack.
        if paren_string == "(":
            stack.append(paren_string)
        # If we are at a right parentheses, we pop one element from the stack.
        if paren_string == ")":
            stack.pop()

    # Return the number of elements in the stack which represents the deepest level of nesting.
    return len(stack)

