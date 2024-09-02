
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
    def count(s):
        return sum(1 if c == '(' else -1 for c in s)

    a, b = lst
    ca, cb = count(a), count(b)
    if ca == cb:
        return 'Yes'
    elif ca < cb:
        return 'No'
    else:
        c = ca - cb
        return 'Yes' if c % 2 == 0 else 'No'
