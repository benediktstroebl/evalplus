from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # the deepest level of nesting of parentheses
    deepest_level = 0
    # the level of nesting of parentheses at the current position of the string
    current_level = 0
    # deepest level of the current group
    max_level = 0
    # the start position of the current group
    start_index = 0
    # the result list
    result = []

    # Note that, since the input has balanced parentheses, the following loops terminate
    for i in range(len(paren_string)):
        # if we encounter an opening paren, update the level of nesting
        if paren_string[i] == '(':
            current_level += 1
            # update the max level for the current group if necessary
            if current_level > max_level:
                max_level = current_level
        # if we encounter a closing paren, update the level of nesting
        elif paren_string[i] == ')':
            current_level -= 1
            # if we are at the end of the string, update the result
            if i == len(paren_string) - 1:
                # update the deepest level of the current group if necessary
                if max_level > deepest_level:
                    deepest_level = max_level
                # update the result for the current group
                result.append(max_level)
        # if we encounter a space and we are not at the end of the string
        elif i < len(paren_string) - 1:
            # update the result for the previous group
            if max_level > deepest_level:
                deepest_level = max_level
            # update the result for the current group
            result.append(max_level)
            # reset the level of nesting
            current_level = 0
            # update the start position of the current group
            start_index = i + 1
            # reset the max level of the current group
            max_level = 0

    # return the final result
    return result

