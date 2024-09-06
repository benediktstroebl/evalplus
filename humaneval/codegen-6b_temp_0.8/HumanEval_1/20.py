from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    s = paren_string.replace(' ', '')
    start_stack = []
    counter = 0
    temp_stack = []
    paren_stack = []
    for c in s:
        if c == '(':
            start_stack.append(counter)
        elif c == ')':
            temp_stack.append(start_stack.pop())
        counter += 1
        # For every open-brace, push it to the stack
        if counter in start_stack:
            paren_stack.append((c, counter))
    # Iterate through the stack and append the proper string
    # Make sure to start at the close parenthesis, when popping
    # instead of popping the first element
    string_list = []
    for c, p in paren_stack:
        if c == ')':
            counter = p
        else:
            while counter != p:
                string_list.append(paren_stack.pop()[0])
                counter = paren_stack.pop()[1]
            string_list.append(c)
    return string_list

