from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # I don't know why you need two stacks to store nesting depth, but I think it's because
    # in the second stack, we need to keep track of the nesting of the first nesting.
    # So we need to keep a list of nesting depths for the first stack, and a list of nesting depths for the second stack

    # I think for the overall complexity, we don't care if we are popping from the first stack when the second stack has
    # more nesting depth. So we can keep a list of the nesting depths for the second stack, but we don't want to keep
    # popping from the second stack when the first stack is empty. So since we can't pop from the first stack, we have to
    # maintain the list of nesting depths for the second stack. If we are popping from the second stack when the first
    # stack has empty, then we are popping from the first stack, *but* of course, that means we are popping from the second
    # stack, as well.
    first_stack = []
    second_stack = []
    max_depth = 0
    depth_counter = 0
    last_depth = 0
    for paren in paren_string:
        if paren == '(':
            first_stack.append(depth_counter)
            depth_counter += 1
            max_depth = max(max_depth, depth_counter)
            last_depth = depth_counter
        elif paren == ')':
            depth_counter -= 1
            second_stack.append(last_depth)
            last_depth = first_stack.pop() + 1
            if first_stack:
                last_depth = first_stack[-1] + 1
            max_depth = max(max_depth, depth_counter)
    return [max_depth, max(second_stack)]

