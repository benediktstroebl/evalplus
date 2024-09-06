from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # The algorithm will use a stack of indices to keep track of the indices of the parens that have not been closed.
    # Each time a new group of unclosed parens is found, the indices of the start and end of that group will be added
    # to the stack. When all the parens have been closed, the stack will contain the start and end indices of all
    # groups of unclosed parens, so we can use those to find the separate groups
    paren_string_stripped = paren_string.replace(' ', '')
    unclosed_paren_indices_stack = []
    for i, paren_char in enumerate(paren_string_stripped):
        if paren_char == '(':
            unclosed_paren_indices_stack.append(i)
        elif paren_char == ')':
            unclosed_paren_indices_stack.pop()

    # The length of the stack should be even, and the length of the longest string in the stack is the length of the
    # longest group of unclosed parens. We can calculate the start and end of each group using these values
    assert len(unclosed_paren_indices_stack) % 2 == 0, 'The string should contain balanced parens'
    unclosed_paren_group_length = len(unclosed_paren_indices_stack) // 2
    unclosed_paren_groups = []
    for i in range(unclosed_paren_group_length):
        start_index = unclosed_paren_indices_stack[2*i]
        end_index = unclosed_paren_indices_stack[2*i+1]
        unclosed_paren_groups.append(paren_string_stripped[start_index:end_index+1])

    return unclosed_paren_groups

