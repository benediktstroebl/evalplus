from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # ------------------------------------------------
    # A recursive solution
    #
    # The idea is that we calculate the max depth of nested parentheses for each group
    # and then take the max out of them.
    # The first thing that comes to mind is to split the string on spaces, and then
    # take the max out of the results of the function called on these groups.
    # ------------------------------------------------
    def nested_parens_depth(string: str) -> int:
        """ Returns the maximum depth of nested parentheses for a given string. """
        # The idea is to use a stack to track the parentheses that we have seen so far
        # and then go over the string and compare the current character to the topmost
        # character on the stack to see if they match or not.
        # If they do match, that means we are inside a set of parentheses, so we add
        # one to the depth of the current string.
        # If they do not match, we pop the topmost element from the stack.
        # This way we can calculate the current depth by the size of the stack at the end
        # of the string.

        stack = []
        max_depth = 0

        for character in string:
            if character == '(':
                stack.append(character)
                max_depth = max(max_depth, len(stack))
            elif character == ')':
                stack.pop()

        return max_depth

    return [nested_parens_depth(group) for group in paren_string.split(' ')]

