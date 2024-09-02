from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Your code here
    return_list = []
    # split by spaces
    paren_string_list = paren_string.split()
    # loop until none in list
    while paren_string_list:
        # list for storing current level of parens
        curr_level = []
        # loop until none in list
        while paren_string_list:
            # list for storing current level of parens
            curr_level_parens = []
            # add i == 0, i == 1, i == 2 etc to list
            for i in range(len(paren_string_list)):
                # if the current char is a '(', append it to curr_level_parens
                if paren_string_list[i] == '(':
                    curr_level_parens.append(paren_string_list[i])
            # add first element of list to curr_level
            curr_level.append(curr_level_parens[0])
            # remove first element of list from paren_string_list
            paren_string_list.pop(0)
            # remove first element of curr_level_parens from curr_level_parens
            curr_level_parens.pop(0)
            # remove first element of paren_string_list from paren_string_list
            paren_string_list.pop(0)
        # append list to return_list
        return_list.append(curr_level)
        # remove 0th element from paren_string_list
        paren_string_list.pop(0)
    return return_list
