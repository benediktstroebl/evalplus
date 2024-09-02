from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    output = []
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            stack.append(0)
        elif paren_string[i] == ")":
            # Find the first ( that comes after the current )
            # Find the index of the corresponding )
            for j in range(i, -1, -1):
                if paren_string[j] == "(":
                    # We have found the first ( so we can get the index of the )
                    # Find the first ( before the )
                    for k in range(j, -1, -1):
                        if paren_string[k] == "(":
                            # We have found the first ( so we can get the index of the )
                            # Find the first ( before the )
                            first_open_paren_index = k
                            break
                    # Find the index of the closing )
                    last_closed_paren_index = j
                    stack_copy = stack[:]
                    while stack_copy:
                        if stack_copy[-1] == 0:
                            first_open_paren_index = j
                            last_closed_paren_index = first_open_paren_index - 1
                            break
                        elif stack_copy[-1] == 1:
                            tmp_stack = stack_copy[:-1]
                            if tmp_stack:
                                if tmp_stack[-1] == 0:
                                    first_open_paren_index = j
                                    last_closed_paren_index = first_open_paren_index - 1
                                    break
                                else:
                                    stack_copy = tmp_stack
                            else:
                                stack_copy = []
                        else:
                            break
                    # Calculate the nesting depth
                    nesting_depth = last_closed_paren_index - first_open_paren_index + 1
                    output.append(nesting_depth)
                    stack = stack_copy
                elif paren_string[j] == ")":
                    stack_copy = stack[:]
                    stack = []
                    break
    return output

