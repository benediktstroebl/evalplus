from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Keep track of the deepest level of nesting of parentheses
    max_nesting_count = 0

    # A count of open parentheses that we encounter while parsing the input string
    # Note that this can be more than one if we encounter multiple groups
    # E.g. in ((())()()) there are two open parentheses
    # We will use this count in order to compute the deepest level of nesting
    open_parens_count = 0

    # A list of the deepest level of nesting of parentheses for each group
    max_nesting_count_list = []

    # Keep track of the current character
    char_index = 0

    while char_index < len(paren_string):
        char = paren_string[char_index]

        if char == '(':
            open_parens_count += 1
        elif char == ')':
            open_parens_count -= 1

        # Check if we encountered the end of a group
        if open_parens_count == 0:
            max_nesting_count = max(max_nesting_count, char_index - 1)

            max_nesting_count_list.append(max_nesting_count)

            # Reset the counters
            open_parens_count = 0
            max_nesting_count = 0

            # Move to the next group
            char_index += 1
            continue

        char_index += 1

    return max_nesting_count_list

