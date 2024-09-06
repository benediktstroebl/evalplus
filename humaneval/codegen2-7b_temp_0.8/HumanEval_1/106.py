from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_chars = [chr(97 + i) for i in range(26)] + [chr(100 + i) for i in range(26)]
    paren_string = paren_string.strip()
    result = []
    cur_stack = []
    for i in range(len(paren_string)):
        cur_chr = paren_string[i]
        if cur_chr in paren_chars:
            cur_stack.append(cur_chr)
        else:
            result.append(''.join(cur_stack))
    
