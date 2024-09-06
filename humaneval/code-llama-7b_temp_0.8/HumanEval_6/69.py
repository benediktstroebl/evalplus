from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Keep a stack of indices that point to the first open paren of the current group.
    # It is needed to compute the deepest level of nesting in the current group.
    current_group_indices = []
    # Keep a list of deepest level of nesting for each group
    output = []

    for i, char in enumerate(paren_string):
        # If there are no open parentheses and we see a close paren,
        # it means that there is no close paren in the current group,
        # so append the current group deepest level of nesting.
        if not current_group_indices and char == ')':
            output.append(i)
            continue
        # If we encounter a close paren, push the current index to the stack
        if char == ')':
            current_group_indices.append(i)
        # If we encounter an open paren, it could be a close paren that
        # is closing the current group, or an open paren that is opening
        # a new group. Hence, we need to check the top of the stack to
        # see if the open paren closes the current group
        if char == '(':
            # If there are open parentheses in the stack, it means that
            # there is an open paren that opens a new group
            if current_group_indices:
                current_group_indices.append(i)
            # If there is no open paren on the stack, it means that
            # the current open paren is closing the previous group
            else:
                # Pop the stack and compute the deepest level of nesting
                deepest_level_of_nesting = i - current_group_indices.pop()
                # Append the result to the output
                output.append(deepest_level_of_nesting)

    return output

