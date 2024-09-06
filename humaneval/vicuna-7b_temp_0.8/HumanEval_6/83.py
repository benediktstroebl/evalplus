from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Create a set to keep track of the maximum nesting for each group.
    nesting_set = set()

    # Start with the maximum nesting as the starting value for the current group.
    nesting = max_nesting

    # Iterate over the string of nested parentheses and handle each group of parentheses separately.
    for char in paren_string:
        if char == '(':
            # Start a new group.
            nesting_set.clear()
        elif char == ')':
            # End a group.
            if nesting_set:
                nesting_set.discard(nesting_set.pop(len(nesting_set) - 1))
            nesting_set.append(nesting)
        else:
            # Add the current character to the current group of nesting.
            nesting_set[len(nesting_set) - 1] += 1

    # Return the maximum nesting for each group, accumulated over all the groups.
    return nesting_set
