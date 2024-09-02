from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # If the input string does not contain a single set of parenthesis, return an empty list.
    if '()' not in paren_string:
        return []

    # Remove trailing and leading spaces
    paren_string = paren_string.strip()
    nested_levels = []

    # For each set of parentheses in the input string, find the deepest level of nesting.
    while '()' in paren_string:
        current_nesting_level = 0
        current_index = 0

        # If the character at the current index is '(', increment the current nesting level by 1.
        # If the character at the current index is ')', decrement the current nesting level by 1.
        while current_index < len(paren_string):
            if paren_string[current_index] == '(':
                current_nesting_level += 1
            elif paren_string[current_index] == ')':
                current_nesting_level -= 1

            # If the current nesting level is 0 and we encounter a closing parenthesis,
            # it means we have reached the end of the current set of parentheses.
            if current_nesting_level == 0 and paren_string[current_index] == ')':
                # Add the nesting level of the current group to the final list and remove the group from the input.
                nested_levels.append(current_nesting_level)
                paren_string = paren_string.replace(paren_string[current_index - 1:current_index + 1], '', 1)

                # Since we removed the last group, reset the index.
                current_index = 0
                break

            current_index += 1

    return nested_levels

