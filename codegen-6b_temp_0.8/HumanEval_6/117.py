from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_brackets = []

    for i, bracket in enumerate(paren_string):
        if nested_brackets and bracket == ')' and nested_brackets[-1] >= i:
            nested_brackets[-1] += 1
        elif bracket == '(':
            nested_brackets.append(i)

    # Converts nested_brackets into a list of 'end' indices for closed parentheses
    end_bracket_indices = [
        i + 1
        for i, bracket_level in enumerate(nested_brackets)
        if bracket_level == max(nested_brackets)
    ]

    # Creates a list of two-item tuples of the start and end indices for each group of nested parentheses
    group_indices = [
        (end_bracket_indices[i], end_bracket_indices[i + 1])
        for i in range(0, len(end_bracket_indices), 2)
    ]

    # Return the max depth of nesting for each group of nested parentheses
    return [max(i[1] - i[0] - 1 for i in group_indices)]

