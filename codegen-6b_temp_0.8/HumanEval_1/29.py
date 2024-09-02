from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    openbraced=[]
    done=False
    for i,c in enumerate(paren_string):
        if c=='(':
            openbraced.append((i,c))
        elif c==')':
            if len(openbraced)==0:
                paren_string = paren_string[:i]+paren_string[i+1:]
                done=True
                break
            else:
                j,closing=openbraced.pop()
                paren_string = paren_string[:j]+paren_string[j+1:i]+paren_string[i+1:]
                done=True
                break
    if not done:
        return [paren_string]
    elif not openbraced:
        return [paren_string[:paren_string.find(')')+1]]
    else:
        return [paren_string]+separate_paren_groups(paren_string[:-1])

