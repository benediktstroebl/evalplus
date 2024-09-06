from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # base case
    if not paren_string:
        return []

    if paren_string[0] == ')':
        return []

    paren_stack = []

    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            paren_stack.append(i + 1)
        elif paren_string[i] == ')':
            # pop off all the open parens off the stack
            while paren_stack:
                open_paren = paren_stack.pop()
                # if the open paren is at the top of the stack, we can start parsing from here,
                # otherwise we need to traverse back.
                if not paren_stack:
                    parse_start_i = i
                    break
                else:
                    if paren_stack[-1] > open_paren:
                        parse_start_i = i
                    else:
                        break

    # get the index to the last open paren
    # if we don't have any open parens, we just go to the end of the string
    while paren_stack:
        open_paren = paren_stack.pop()
        if not paren_stack:
            parse_end_i = len(paren_string)
        else:
            if paren_stack[-1] > open_paren:
                parse_end_i = paren_stack[-1]
            else:
                parse_end_i = len(paren_string)

    # parse out the string from the first index to the last index
    return parse_string(paren_string, parse_start_i, parse_end_i)

