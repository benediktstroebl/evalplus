
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
    if n < 2:
        return 'No'
    m = n // 2
    if lst[0][0] == lst[n//2][0] and lst[0][1] == lst[n//2][1]:
        for i in range(m, n):
            if lst[i][0] == lst[i+1][0]:
                return 'No'
    return 'Yes'

test = [
    ['(', ')'],
    ['(', '(', ')'],
    ['(', '(', '(', '(', '(', ')'), ')'],
    ['(', '(', '(', '(', '(', '(', '(', '(', ')'), ')']
]

for t in test:
    print(t, match_parens(t))