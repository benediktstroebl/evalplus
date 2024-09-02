
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
    for i in range(len(lst[0])):
        if lst[0][i] == '(':
            left = lst[0][:i]
            right = lst[0][i + 1:]
            if not match_parens(left) or not match_parens(right):
                return 'No'
            lst[0] = lst[0][:i] + lst[0][i + 1:]
        else:
            if lst[0][-1]!= '(':
                return 'No'
    return 'Yes'

