
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

    pairs = {}
    for i, paren in enumerate(lst[0]):
        if paren in lst[1] and i in pairs:
            pairs[i].append(paren)
        elif paren in lst[1] and i not in pairs:
            pairs[i] = [paren]
    for key, val in pairs.items():
        if val[0] not in lst[0] and val[1] not in lst[1]:
            return 'No'
    return 'Yes'
