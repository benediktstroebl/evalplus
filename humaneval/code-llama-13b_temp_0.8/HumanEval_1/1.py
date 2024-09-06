from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # solution 1
    brace_list = []
    for i in range(0, len(paren_string)):
        if paren_string[i] != ' ' and paren_string[i - 1] != ' ':
            if paren_string[i] == '(':
                brace_list.append('(')
            elif paren_string[i] == ')':
                if len(brace_list) > 0 and brace_list[-1] == '(':
                    brace_list.pop()
                    brace_list.append(')')
    return brace_list
    # solution 2
    # open_stack, close_stack = [], []
    # open_brace_index = [i for i, c in enumerate(paren_string) if c == '(']
    # close_brace_index = [i for i, c in enumerate(paren_string) if c == ')']
    # for open_index, close_index in zip(open_brace_index, close_brace_index):
    #     open_stack.append(open_index)
    #     close_stack.append(close_index)
    # return [paren_string[i:j + 1] for i, j in zip(open_stack, close_stack)]

