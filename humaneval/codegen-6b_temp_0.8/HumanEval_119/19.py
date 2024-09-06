
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
    s = lst[0]
    t = lst[1][:-1]
    while len(s) > 0:
        if s[0] == ')':
            return 'No'
        if t[0] == '(':
            t = t[1:]
        else:
            if len(t) > 0:
                t = t[1:]
            else:
                return 'No'
        s = s[1:]
    return 'Yes'

