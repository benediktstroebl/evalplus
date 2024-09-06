
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
    def check_parens(open, close, lst):
        if open == close:
            return True
        return False

    i, j = 0, len(lst[0])-1
    while i < j:
        if check_parens(lst[0][i], lst[1][j], lst):
            i += 1
        else:
            j -= 1
    if i == j:
        return True
    return False

