from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # the list of deepest nesting level
    res = []

    # this function operates on the index of the string, and keep track of the current deepest nesting level
    def count_parens(idx: int, deepest_level: int) -> int:
        nonlocal res
        if paren_string[idx] == '(':
            # if we encounter (, increment the deepest level
            deepest_level += 1
        elif paren_string[idx] == ')':
            # if we encounter ), decrement the deepest level
            deepest_level -= 1
        else:
            raise ValueError('Invalid character found in the string.')
        if idx == len(paren_string) - 1:
            # if we reach the end of the string, update the list with the max value
            res.append(deepest_level)
        else:
            # if we are not at the end of the string, keep calling the function on the next character,
            # and update the max of the current value with the returned value
            return max(count_parens(idx + 1, deepest_level), deepest_level)
    # call the function on the first index, and return the list
    count_parens(0, 0)
    return res

