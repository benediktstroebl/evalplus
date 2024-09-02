
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
    open_parens = '('
    close_parens = ')'

    def _is_good(s):
        if s == '':
            return True
        if s[0] == open_parens:
            return _is_good(s[1:])
        if s[0] == close_parens:
            return False
        return _is_good(s[1:])

    return 'Yes' if _is_good(lst[0]) and _is_good(lst[1]) else 'No'

