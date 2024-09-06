from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # a recursive function to calculate the level of nesting of parenthesis
    def nest_level(input_string: str) -> int:
        # initializing the level of nesting to 0
        level = 0
        # going through each character of the string
        for char in input_string:
            # if character is opening parenthesis increase level by 1
            if char == "(":
                level += 1
            # if character is closing parenthesis decrease level by 1
            else:
                level -= 1
        return level

    # initializing a list to store the level of nesting of each group of parenthesis
    result = []
    # going through each group of parenthesis separated by spaces
    for group in paren_string.split():
        # calculating the level of nesting of each group
        level = nest_level(group)
        # appending the result to the result list
        result.append(level)
    # returning the result
    return result

