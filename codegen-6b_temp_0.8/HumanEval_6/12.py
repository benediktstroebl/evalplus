from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # if len(paren_string) == 0:
    #     return []

    # stack = 0
    # max_stack = 0
    # open_parens = 0
    # balance = 0
    # paren_string = paren_string.replace('(', '')
    # paren_string = paren_string.replace(')', '')

    # for char in paren_string:
    #     if char == '(':
    #         stack += 1
    #         open_parens += 1
    #         max_stack = max(stack, max_stack)
    #     elif char == ')':
    #         stack -= 1
    #         balance += 1
    #         if max_stack - stack == 1:
    #             # print(stack, max_stack, open_parens)
    #             open_parens += balance
    #         max_stack = max(stack, max_stack)
            
    # return [max_stack, open_parens]

    # don't actually need to solve the problem with DP
    # if len(paren_string) == 0:
    #     return []

    solution = []

    stack = []
    for i in range(len(paren_string)):
        character = paren_string[i]
        if character == '(':
            stack.append(character)
        else:
            if not stack:
                solution.append(i)
            else:
                stack.pop()
    return solution

    # def has_open_paren(string: str) -> bool:
    #     """
    #     if string is empty, return false
    #     if the last character is not a parenthesis, return false
    #     if the last character is a parenthesis, return true
    #     """
    #     if not len(string):
    #         return False
    #     else:
    #         last = string[-1]
    #         if last == ')':
    #             return True
    #         else:
    #             return False
    
    # def get_max_depth(string: str) -> int:
    #     """
    #     if string