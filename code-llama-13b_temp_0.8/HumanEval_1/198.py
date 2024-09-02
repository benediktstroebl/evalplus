from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    ...
    # Example code below:
    # return_list = []
    # start_idx = 0
    # brace_ctr = 0
    # for idx, brace in enumerate(paren_string):
    #     if brace == '(':
    #         brace_ctr += 1
    #     elif brace == ')':
    #         brace_ctr -= 1
    #     if brace_ctr == 0 and start_idx != idx:
    #         return_list.append(paren_string[start_idx: idx + 1])
    #         start_idx = idx + 1
    # return return_list
