from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # plan:
    # count how many '(' and ')' are there
    # if there are more '(' than ')', the number of nested parentheses is the total of '('
    # if there are more ')' than '(' the number of nested parentheses is the total of ')'
    # if there are same number of '(' and ')', the number of nested parentheses is half the total of ')'

    # maintain 2 variables to store current level of nesting (starting at 0)
    # and total number of '(' and ')'
    nesting = 0
    open_paren_count = 0
    closed_paren_count = 0

    results = []

    for character in paren_string:
        if character == '(':
            open_paren_count += 1
            nesting += 1
        elif character == ')':
            closed_paren_count += 1
            nesting -= 1
        else:
            raise ValueError(f"Invalid character {character} in string {paren_string}")

        if closed_paren_count > open_paren_count:
            results.append(closed_paren_count)
            open_paren_count = 0
            closed_paren_count = 0
            nesting = 0

    return results

