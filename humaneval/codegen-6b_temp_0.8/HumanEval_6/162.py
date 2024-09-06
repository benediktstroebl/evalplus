from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # The characters which indicate that a parenthesis is nested inside another
    DELIMS = {'(', ')', '{', '}', '[', ']', '<', '>'}
    stack = []
    curr_level = 0

    for index, char in enumerate(paren_string):
        if char in DELIMS:
            stack.append(char)
            curr_level += 1
        elif char == ')':
            # Pop until we find an open paren
            while len(stack) > 0 and stack[-1] != '(':
                curr_level -= 1
                stack.pop()
            if len(stack) == 0:
                curr_level = 0
                break
            else:
                stack.pop()
                curr_level -= 1
        elif char == '}':
            # Pop until we find an open paren
            while len(stack) > 0 and stack[-1] != '{':
                curr_level -= 1
                stack.pop()
            if len(stack) == 0:
                curr_level = 0
                break
            else:
                stack.pop()
                curr_level -= 1
        elif char == ']':
            # Pop until we find an open paren
            while len(stack) > 0 and stack[-1] != '[':
                curr_level -= 1
                stack.pop()
            if len(stack) == 0:
                curr_level = 0
                break
            else:
                stack.pop()
                curr_level -= 1
        elif char == '<':
            # Pop until we find an open paren
            while len(stack) > 0 and stack[-1] != '<':
                curr_level -= 1
                stack.pop()
            if len(stack) == 0:
                curr_level = 0
                break
            else:
                stack.pop()
                curr_level -= 1
        else:
            # Pop until we find an open paren
            while len(stack) > 0 and stack[-1] != '>':
                curr_level -= 1
                stack.pop()