from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Base case for recursion
    if len(paren_string) == 0:
        return []

    # Indices of opening and closing parentheses in string
    start_idx = paren_string.find('(')
    end_idx = paren_string.find(')')
    paren_string = paren_string[:end_idx]

    # While there are still more parentheses to process
    while start_idx >= 0:
        # Recursively call this function on all the nested parentheses
        deeper_max_level = parse_nested_parens(paren_string)
        # Append the max level of nesting for the outermost parentheses
        deeper_max_level.append(max(deeper_max_level) + 1)
        # Update the string with the outermost parentheses removed
        paren_string = paren_string[end_idx + 1:]
        start_idx = paren_string.find('(')
        end_idx = paren_string.find(')')
        paren_string = p
