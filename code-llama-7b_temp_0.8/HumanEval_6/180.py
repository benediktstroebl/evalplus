from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # 1. Declare an empty list to store the max_depths
    max_depths = []

    # 2. Traverse the string
    for i in range(len(paren_string)):

        # 3. If we come across a left paren then
        #    a. increment the counter by 1
        #    b. initialize the max_depth as 1
        if paren_string[i] == '(':
            counter = 1
            max_depth = 1

        # 4. If we come across a right paren then
        #    a. decrement the counter by 1
        #    b. update the max_depth if necessary
        #    c. If the counter is now zero, it means that we have seen the last paren in a group and
        #       we can now append the max_depth to our list of max_depths
        if paren_string[i] == ')':
            counter -= 1
            if counter == 0:
                max_depths.append(max_depth)
                max_depth = 0
            else:
                max_depth += 1
    return max_depths

