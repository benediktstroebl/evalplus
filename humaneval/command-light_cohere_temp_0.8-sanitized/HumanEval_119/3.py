def match_parens(s):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is determine if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is expected to be good if and only if all parentheses in S
    are balanced.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    s1 = '()()'
    s2 = ')'
    return 'Yes' if all(balance(p) for p in s1+s2) else 'No'
def balance(p):
    '''
    You are given an open or close parentheses '(' or ')'
    You need to return True if the parentheses is balanced, and False otherwise.
    Examples:
    balance('()') == True
    balance('())' == False
    '''
    if p == '(': return True
    else: return False
    return None