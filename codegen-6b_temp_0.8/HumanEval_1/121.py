from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parsed_string = []
    # You want to keep track of the balance of the pairs of braces.
    # For every character in paren_string, if the balance is zero or less
    # you want to add it to the result, and if it is positive you want to
    # add it to the stack.
    # If the balance is negative, add it to the result and add a
    # ( or { to the stack. The stack will always have an opening parentheses
    # at the top.
    # If the balance is zero, remove a matching closing parentheses from
    # the stack, and add it to the result.
    # Time - O(n)
    # Space - O(n)

    # balanced = 0
    # result = []
    # stack = []
    # for char in paren_string:
    #     if char == '(':
    #         stack.append('(')
    #         balanced += 1
    #     elif char == ')':
    #         balanced -= 1
    #         if len(stack) > 0 and stack[-1] == '(':
    #             del stack[-1]
    #         else:
    #             result.append('()')
    #     elif char == '{':
    #         stack.append('{')
    #         balanced += 1
    #     elif char == '}':
    #         balanced -= 1
    #         if len(stack) > 0 and stack[-1] == '{':
    #             del stack[-1]
    #         else:
    #             result.append('{}')
    #     elif char == ' ':
    #         pass
    #     else:
    #         raise ValueError(f'{char} is not a valid character')

    #     if balanced == 0:
    #         result.append(stack)

    # return result

    # Part 2. Time - O(n)
    # Part 2. Space - O(n)
    result = []
    stack = []
    for ch in paren_string:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        el