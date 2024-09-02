
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
    s = lst[0] + lst[1]
    if len(s) == 0:
        return 'Yes'
    if len(s) == 1:
        return 'No'
    if s.count('(') != s.count(')'):
        return 'No'
    if s.count('(') == 0 and s.count(')') == 0:
        return 'Yes'
    if s.count('(') == 0 and s.count(')') > 0:
        return 'No'
    if s.count('(') > 0 and s.count(')') == 0:
        return 'No'
    if s.count('(') > 0 and s.count(')') > 0:
        if s.index(')') < s.index('('):
            return 'No'
        if s.index(')') == s.index('('):
            return 'Yes'
        if s.index(')') > s.index('('):
            s = s[s.index(')') + 1:] + s[:s.index(')')]
            return match_parens([s[:len(s) // 2], s[len(s) // 2:]])

