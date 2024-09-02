
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
    # lst = lst[0].strip()
    # r = lst[1].strip()
    s = ''
    for c in lst[0]:
        if c != '(' and c != ')':
            s += c
    if len(s) != len(lst[1]):
        return 'No'

    l = len(s)
    s += ')' * (l - len(s))
    s = s.split('(')
    s.reverse()
    r = ''
    for c in lst[1]:
        if c != ')':
            r += c
    r += '(' * (l - len(r))
    r = r.split(')')
    r.reverse()
    for i in range(len(r)):
        if s[i].count('(') != r[i].count(')'):
            return 'No'
    return 'Yes'

