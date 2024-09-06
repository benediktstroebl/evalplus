
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
    open_parens = ['(', '[', '{']
    close_parens = [')', ']', '}']

    def test(a, b):
        while a < len(a) and b < len(b):
            if a[a] in close_parens and b[b] in open_parens:
                a += 1
                b += 1
            elif b[b] in close_parens and a[a] in open_parens:
                b += 1
            else:
                return False
        return a == len(a) and b == len(b)
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if test(lst[i], lst[j]):
                return 'Yes'
    return 'No'

