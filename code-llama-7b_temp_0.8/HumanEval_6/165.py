from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Replace all '()' with '#'
    new_str = paren_string.replace('()', '#')

    # Split the string by spaces
    str_lst = new_str.split()

    # Appending the last item to the string list
    str_lst.append(str_lst[-1] + '#')

    # Initialize the list to return
    count_lst = []

    # Loop through the string list
    for item in str_lst:
        count = 0
        # Loop through the string item
        for char in item:
            # If char is '(', then increase the count
            if char == '(':
                count += 1
            # If char is ')', then decrease the count
            elif char == ')':
                count -= 1
        # Add the count to the list to return
        count_lst.append(count)

    return count_lst

