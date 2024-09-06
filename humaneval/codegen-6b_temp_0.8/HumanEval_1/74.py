from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    dict = {}
    for i in range(len(paren_string)):
        if paren_string[i] in dict:
            dict[paren_string[i]].append(i)
        else:
            dict[paren_string[i]] = [i]
    stack = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            stack.append(i)
        elif paren_string[i] == ')' and len(stack) > 0:
            start = stack.pop()
            end = i
            string = paren_string[start+1:end]
            string = string.strip()
            print(string)
            i = end + 1
        else:
            i += 1
