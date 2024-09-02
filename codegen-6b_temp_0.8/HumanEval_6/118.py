from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Set the index of the first character and the number of open parens
    start_index, num_open_parens = 0, 0
    # Set the index of the last character and the number of open parens
    last_index, num_open_parens = len(paren_string) - 1, 0
    # Count the number of open parens at the current index
    num_open_parens = count_open_parens(paren_string, start_index)

    # Initialize the output list with an empty string
    output = [''] * num_open_parens

    # For the first level, the max size of the string is the length of the input,
    # and the nesting level is 1 (maximum nesting level)
    max_size = len(paren_string)
    max_nesting_level = 1

    # Iterate over the string from left to right
    for i in range(len(paren_string)):
        # If an open paren is encountered, increase the nesting level
        if paren_string[i] == '(':
            num_open_parens += 1
            # Increase the max size when a new level is found
            if i - start_index > max_size:
                max_size = i - start_index
                # Set the current index as the start index
                start_index = i
            # Increase the max nesting level when a new level is found
            elif i - start_index == max_size:
                max_nesting_level += 1
                # Set the current index as the start index
                start_index = i

        # If a close paren is encountered, decrease the max nesting level
        elif paren_string[i] == ')':
            num_open_parens -= 1
            # If the max nesting level is 1, the output[0] is the max nesting level,
            # and the current index is the start index and is not the last index
            if max_nesting_level == 1 and i != last_index:
                output[0] = i + 1 - start_index
                # Set the start index as the current index
                start_index = i + 1
            # If the max nesting level is