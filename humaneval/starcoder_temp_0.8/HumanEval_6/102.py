from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # your code here

    # Base case: the paren string is empty
    if len(paren_string) == 0:
        return []

    # Recursive case: the last character of the paren string is an end paren
    elif paren_string[-1] == ")":
        # Slice the paren string from 0 to the length of paren string - 1, the last character is an end paren,
        # and get the list of nested parentheses without the last character
        nested_parens = parse_nested_parens(paren_string[:len(paren_string) - 1])

        # Append 1 to the list of nested parentheses
        nested_parens.append(1)

        return nested_parens

    # Recursive case: the last character of the paren string is an open paren
    else:
        # Slice the paren string from 0 to the length of paren string - 1, the last character is an open paren
        # and get the list of nested parentheses without the last character
        nested_parens = parse_nested_parens(paren_string[:len(paren_string) - 1])

        # Append the last level of nesting to the list of nested parentheses
        nested_parens.append(nested_parens[-1] + 1)

        return nested_parens

