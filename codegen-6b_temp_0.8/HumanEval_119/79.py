
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
    def add(st, s, f):
        if f:
            return st + s[1:]
        else:
            return st + s[1:-1]

    if lst[0] == ')' or lst[-1] == '(':
        return 'No'

    stack = []
    for p in lst:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return 'No'
            else:
                stack.pop()

    return 'Yes' if not stack else 'No'

