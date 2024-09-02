
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
    n = len(lst)
    if n == 0:
        return 'No'
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if j < i:
                # try to concatenate the remaining strings to the right of i
                s = lst[i+1] + lst[j]
                if not match_parens(lst[:i]+[s] + lst[j+1:]) == 'Yes':
                    return 'No'
    return 'Yes'
