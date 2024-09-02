
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
    # by zueve
    def isgood(s):
        if len(s) % 2:
            return False
        while '()' in s:
            s = s.replace('()', '')
        return not s

    def combo(s1, s2):
        for i in s1:
            if i in s2:
                return isgood(s1[:s1.index(i)] + s2[s2.index(i) + 1:])
        return False

    return 'No' if len(lst) == 1 or not combo(*lst) else 'Yes'
