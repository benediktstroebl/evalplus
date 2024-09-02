from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    start = 0
    end = 1
    res = []
    # 1. loop through the string
    # 2. increment end until you find a closed parenthesis
    # 3. keep track of the last open parenthesis
    # 4. start new string from last open parenthesis
    # 5. when you find a closed parenthesis, append the substring from the last open to the closed
    #    parenthesis, then increase the start to the closed parenthesis + 1
    # 6. repeat until all strings are found
    while end < len(paren_string):
        if paren_string[end] == '(':
            last_open = end
        if paren_string[end] == ')':
            res.append(paren_string[last_open:end+1])
            start = end + 1
        end += 1
    return res

