
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
    if len(lst) != 2: return 'No'
    a, b = lst
    if not a or not b: return 'No'
    cnt_a = cnt_b = 0
    for i in a:
        if i == '(': cnt_a += 1
        else: cnt_a -= 1
    for i in b:
        if i == '(': cnt_b += 1
        else: cnt_b -= 1
    if cnt_a + cnt_b == 0:
        return 'Yes'
    return 'No'
