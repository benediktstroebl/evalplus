
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

    if not lst:
        return 'Yes'

    out = []
    for item in lst:
        if item == ')':
            out.append(item)
        else:
            if out[-1]!= '(' and out[-1]!= ')' and out:
                return 'No'
            out.append(item)

    if len(out) % 2 == 0 or out[-1] == '(' or out[-1] == ')' or len(out) == 1:
        return 'Yes'
    else:
        return 'No'

