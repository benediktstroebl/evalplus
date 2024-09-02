from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # for i in range(len(paren_string)):
    #    if paren_string[i] == '(':
    #        a.append(i)
    #    elif paren_string[i] == ')':
    #        a.append(i)
    # print(a)
    # left_stack = []
    # right_stack = []
    #
    # for i in range(len(a)):
    #     if paren_string[i] == '(':
    #         left_stack.append(i)
    #     if paren_string[i] == ')':
    #         if left_stack == []:
    #             right_stack.append(i)
    #         else:
    #             left_stack.pop()
    #
    # groups = []
    #
    # for i in range(len(left_stack)):
    #     groups.append(paren_string[left_stack[i]:right_stack[i]+1])
    #
    # print(groups)
    # return [groups[i] for i in range(len(groups)) if i%2 == 0]

    stack = []
    groups = []
    for i in paren_string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack == []:
                groups.append(i)
            elif stack[-1] == "(":
                groups.append(i)
            else:
                stack.pop()

    return [groups[i] for i in range(len(groups)) if i % 2 == 0]
