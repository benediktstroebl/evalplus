from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    has_paren = False
    single_parentheses = False
    left_paren = 0
    right_paren = 0
    inside = False
    group = []

    for i, char in enumerate(paren_string):
        if char == '(':
            left_paren += 1
            group.append(i)
            if inside:
                single_parentheses = True
            inside = True
        elif char == ')':
            right_paren += 1
            if left_paren != right_paren:
                list_copy = group.copy()
                list_copy.reverse()
                for j in list_copy:
                    del group[group.index(j)]
                result.append(''.join(group))
                inside = False
                group = []
            elif not single_parentheses:
                del group[group.index(i)]
                result.append(''.join(group))
                inside = False
                group = []

    if single_parentheses:
        list_copy = group.copy()
        list_copy.reverse()
        for j in list_copy:
            del group[group.index(j)]
        result.append(''.join(group))
    else:
        del group[group.index(i)]
        result.append(''.join(group))

    return result

