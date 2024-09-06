
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

    
    parens = [list(i) for i in lst]
    curr = []
    for p in parens:
        if not curr:
            curr.append(p)
        else:
            if len(curr[-1]) > len(p):
                curr.append(p)
            else:
                if p == ')' and curr[-1][-1] == '(':
                    curr[-1].pop(-1)
                else:
                    return 'No'
    if not curr:
        return 'Yes'
    return 'No'

