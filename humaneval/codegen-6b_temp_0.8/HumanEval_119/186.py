
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    open_to_close = {'(':')', '{':'}', '[':']'}
    close_to_open = {')':'(', '}':'{', ']':'['}
    stack = []
    for c in lst:
        if c in open_to_close:
            stack.append(c)
        elif c in close_to_open:
            if not stack:
                return 'No'
            if c != close_to_open[stack.pop()]:
                return 'No'
    if stack:
        return 'No'
    return 'Yes'
