from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Find the first left parenthesis,
    # then recursively parse the inside of the parenthesis
    # and add those to a list.  Then find the next right parenthesis and recursively parse the inside of that.
    # Add those to a list and so on until you get to the end of the input.
    # Return the list of depths.

    depth_list = []

    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            depth_list.append(i)
    first_left = depth_list[0]
    del depth_list[0]
    parse_paren_string = paren_string[first_left]
    while parse_paren_string != ")":
        for i in range(len(parse_paren_string)):
            if parse_paren_string[i] == '(':
                depth_list.append(i)
        first_left = depth_list[0]
        del depth_list[0]
        parse_paren_string = paren_string[first_left]
    return depth_list

    # my_depth_list = []
    # for i in range(len(paren_string)):
    #     if paren_string[i] == '(':
    #         my_depth_list.append(i)
    #     elif paren_string[i] == ')':
    #         depth = my_depth_list.pop()
    #         my_depth_list = [depth]

