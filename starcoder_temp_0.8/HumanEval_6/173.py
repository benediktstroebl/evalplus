from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Initialize
    parsed_string = ''
    output = []
    # Traverse through each char in the input string
    for char in paren_string:
        # If a close paren
        if char == ')':
            # Increment parsed string count
            parsed_string += char
            # If the count is 2 or more, pop the last element
            if parsed_string.count('(') >= 2:
                parsed_string = parsed_string[1:]
            # If the count is 0, add the count to the output list
            if parsed_string.count('(') == 0:
                output.append(len(parsed_string))
                parsed_string = ''
        # Else if an open paren
        elif char == '(':
            # Add the char to the parsed string
            parsed_string += char
    return output

