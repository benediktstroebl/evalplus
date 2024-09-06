from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    current_parens = 0
    max_nest = 0
    nestings = []
    parens = ['(', ')']
    nesting_numbers = []
    current_nesting = 0

    for paren in paren_string:
        if paren in parens:
            if paren == '(':
                current_nesting += 1
                nestings.append(current_nesting)
                current_nesting_number = 1
                current_parens = 1
            if paren == ')':
                current_nesting -= 1
                current_nesting_number = 1
                current_parens = 0

                # Store the nesting number for this group
                nesting_numbers.append(current_nesting_number)

                # If we had a nested group, we need to account for it
                if current_nesting > 0:
                    nestings[current_nesting - 1] = nestings[current_nesting - 1] * current_nesting_number

                # Reset the nesting number for the next group
                current_nesting_number = 1
    
    return nestings

