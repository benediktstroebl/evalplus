from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Solution 1: Brute Force
    # num_parens_list = []
    # for paren_str in paren_string.split():
    #     max_count = 0
    #     for i in range(len(paren_str)):
    #         if paren_str[i] == '(':
    #             max_count += 1
    #         elif paren_str[i] == ')':
    #             max_count -= 1
    #     num_parens_list.append(max_count)
    # return num_parens_list

    # Solution 2: Stack
    # string_stack = []
    # num_parens_list = []
    # for char in paren_string:
    #     if char == '(':
    #         string_stack.append(char)
    #     elif char == ')':
    #         if string_stack:
    #             string_stack.pop()
    #         else:
    #             num_parens_list.append(0)
    #     else:
    #         pass
    # num_parens_list.extend([len(string_stack)]*len(string_stack))
    # return num_parens_list

    # Solution 3: Brute Force + Stack
    # num_parens_list = []
    # for paren_str in paren_string.split():
    #     max_count = 0
    #     string_stack = []
    #     for i in range(len(paren_str)):
    #         if paren_str[i] == '(':
    #             string_stack.append(paren_str[i])
    #         elif paren_str[i] == ')':
    #             if string_stack:
    #                 string_stack.pop()
    #             else:
    #                 num_parens_list.append(0)
    #         else:
    #             pass
    #     num_parens_list.append(len(string_stack))
    # return num_parens_list

    # Solution 4: Brute Force + D
