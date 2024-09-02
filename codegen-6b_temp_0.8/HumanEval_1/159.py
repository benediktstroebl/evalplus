from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    separated_from = set()

    # if the char is close bracket, save it to a set
    # this is used by the unbalanced case, where we only have new open bracket to check for it
    # this case is also used for the unbalanced case, where we have new close bracket to see if we need to
    # save it to set
    for i, char in enumerate(paren_string):
        if char == ')':
            separated_from.add(i)

    # for each set of unbalanced open brackets, close them and add the result to the corresponding separated list
    # also update the unbalanced set where the closed brackets were
    res = []
    unbalanced_closing = set()
    for i, char in enumerate(paren_string):
        if char == '(':
            if i not in separated_from:
                unbalanced_closing.add(i)
            else:
                res.append(')')
        elif char == ')':
            if i in unbalanced_closing:
                # we have a pair of matching closing brackets, we need to close them
                # add that to the unbalanced closing set
                res.append(')')
                del unbalanced_closing[unbalanced_closing.index(i)]
            else:
                # we have an opening bracket, but there is no matching close bracket.
                # we need to close it
                unbalanced_closing.add(i)
        else:
            continue

    # add any leftover unbalanced brackets, they will be left in the result
    for i in unbalanced_closing:
        res.append(')')

    return res

