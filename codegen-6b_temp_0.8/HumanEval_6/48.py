from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Map opening indexes to closing indexes
    index_map = {}

    # Keep track of current level of nesting
    current_level = 0

    # Length of string
    len_str = len(paren_string)

    # The index of the character before the current character
    previous_index = -1

    # Iterate through each character
    for index in range(len_str):

        # If current character is '(', increment current_level and increment previous_index
        if paren_string[index] == '(':
            current_level += 1
            previous_index = index

        # If current character is ')', decrement current_level and decrement previous_index
        elif paren_string[index] == ')':
            current_level -= 1
            previous_index = index

            # If the current index is also the first index and current_level is 0, make previous_index equal to index
            if index == 0 and current_level == 0:
                previous_index = index

        # Add the index of the opening index if the current character is not a closing character
        if paren_string[index] != ')' and paren_string[index] != '(':
            if previous_index in index_map:
                index_map[previous_index] = index
            else:
                index_map[previous_index] = index

    # If current level is still greater than 0, return -1
    if current_level > 0:
        return -1

    # Iterate through each key in the index map
    for key in sorted(index_map.keys()):

        # If key is the last index, current_level is the index of the last index
        if key == len_str - 1:
            current_level = index_map[key]

    # Get the index of the first index after the last index for which nesting level is 0
    for key in sorted(index_map.keys()):

        # If current level is zero, return the index of the key
        if index_map[key] == current_level:
            return key

    # If current_level is still greater than 0, return -1
    return -1

