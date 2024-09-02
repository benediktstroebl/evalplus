from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # if not isinstance(paren_string, str):
    #     raise TypeError("Input must be a string")
    # # print(paren_string)
    #
    # stack = list()
    # groups = list()
    # group = list()
    # for paren in paren_string:
    #     if paren == '(':
    #         stack.append(paren)
    #         # print(stack)
    #     elif paren == ')':
    #         group.append(stack.pop())
    #         # print(group)
    #         if len(stack) == 0:
    #             groups.append(group)
    #             # print(groups)
    #             group = list()
    #
    # return ["".join(group) for group in groups]

    # This solution uses a stack to keep track of all the opening parentheses.
    # When a closing parenthesis is reached, a group is completed and is added to the output list.
    # The list of groups is then returned.

    stack = list()
    group = list()
    groups = list()

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                stack.append(char)
            if not stack:
                groups.append(''.join(group))
                group = list()
        else:
            group.append(char)
    return groups

