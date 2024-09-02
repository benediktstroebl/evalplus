from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    index = 0
    if paren_string is None:
        return None
    if paren_string == '':
        return ['']
    results = []
    while index < len(paren_string):
        if paren_string[index] == '(':
            paren_group = ''
            count = 1
            # save index into the loop
            save = index
            while count > 0:
                index += 1
                char = paren_string[index]
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count == 0 and save != index:
                    paren_group += paren_string[save:index + 1]
                    index += 1
                    break
                elif count == 0 and save == index:
                    paren_group += paren_string[save:index]
                    index += 1
            results.append(paren_group)
    return results
