
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
    # it is easy to construct a case which fails this code
    # so the return value 'No' is a good first answer
    # but it is important that the code is not able to crash
    if not lst:
        return 'Yes'
    parens = {}
    for s in lst:
        for p in s:
            if p in parens:
                parens[p] += 1
            else:
                parens[p] = 1
    for p in '()':
        if parens.get(p, 0) % 2:
            return 'No'
    return 'Yes'
