from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # end_idx = 0
    # start_idx = 0
    # last_start_idx = 0
    # last_end_idx = 0
    # depth_counter = 0
    # depth = 0
    # i = 0
    # depth_list = []
    # while i < len(paren_string):
    #     if paren_string[i] == '(':
    #         depth += 1
    #         depth_counter += 1
    #         end_idx = i
    #     elif paren_string[i] == ')':
    #         depth -= 1
    #         depth_counter -= 1
    #         start_idx = i
    #         # In case of nested parentheses, last_start_idx and last_end_idx are the dates of the last deep nested parentheses
    #         end_idx = i
    #         if depth_counter == 0 and depth > 0:
    #             last_start_idx = start_idx
    #             last_end_idx = end_idx
    #     i += 1
    #
    # if depth_counter == 0:
    #     depth_list.append(depth)
    #     depth_list.append(last_start_idx)
    #     depth_list.append(last_end_idx)
    #     depth_list.sort()
    #     return depth_list
    # else:
    #     depth_list.append(depth)
    #     return depth_list
    def is_open_paren(char: str) -> bool:
        return char == '('

    def is_close_paren(char: str) -> bool:
        return char == ')'

    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return None
            last_char = stack.pop()
            while not is_open_paren(last_char):
                prev_char = stack.pop()
                last_char = prev_char
            stack.pop()
    return None

