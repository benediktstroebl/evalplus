from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []
    paren_stack = []
    paren_stack.append(paren_string[0])
    paren_index = 0
    results = []
    while paren_index < len(paren_string):
        if paren_stack[-1] in {'(', '{'}:
            paren_stack.append(paren_string[paren_index])
            paren_index += 1
        elif paren_stack[-1] in {'[', '{'}:
            paren_stack.append(paren_string[paren_index])
            paren_index += 1
        elif paren_stack[-1] == ')':
            if paren_string[paren_index] == '(':
                paren_stack.pop()
                paren_index += 1
            elif paren_string[paren_index] == ')':
                paren_stack.pop()
                paren_index += 1
        elif paren_stack[-1] == '}':
            if paren_string[paren_index] == '{':
                paren_stack.pop()
                paren_index += 1
            elif paren_string[paren_index] == '}':
                paren_stack.pop()
                paren_index += 1
        elif paren_stack[-1] == ']':
            if paren_string[paren_index] == '{':
                paren_stack.pop()
                paren_index += 1
            elif paren_string[paren_index] == ']':
                paren_stack.pop()
                paren_index += 1
    if len(paren_stack) == 0:
        return results
    elif len(paren_stack) == 1:
        paren_stack.pop()
        paren_string = ''.join(paren_stack)
        paren_string = paren_string.replace('()', '')
        if paren_string == "":
            return results
        results.append(paren_string)
        return results
    else:
        for i in range(len(paren_stack)):
            if paren_stack[-i - 1]