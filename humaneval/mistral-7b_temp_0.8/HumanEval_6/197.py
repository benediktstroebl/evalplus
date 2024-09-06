from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # use Python's string indexing to get a list of parens
    paren_list = list(paren_string)

    # use Python's builtin enumerate to get the index of each list item
    paren_idx = [idx for idx, item in enumerate(paren_list)]

    # for each nested parens group, append the deepest level of nesting of parentheses
    output = []
    for group in paren_list:
        # at each group, append the deepest level of nesting of parentheses to the output list
        output.append(count_nesting_level(paren_idx, group))

    return output

