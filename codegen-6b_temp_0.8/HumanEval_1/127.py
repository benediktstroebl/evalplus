from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []
    # DFS
    results = []
    visited_paren = set()
    for i, s in enumerate(paren_string):
        if s == ')':
            # if there was an open parenthesis, we record that we're done
            if i in visited_paren:
                results.append(''.join(paren_string[:i+1]))
            # going backward, keep popping the last element from the stack
            while True:
                if len(visited_paren) == 0:
                    break
                if visited_paren[-1] == i - 1:
                    visited_paren.pop()
                else:
                    break
    results.append(''.join(paren_string))
    return results

