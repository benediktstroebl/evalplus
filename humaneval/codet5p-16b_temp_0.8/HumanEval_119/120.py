
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

    
    def match(s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        if l1 + l2 == 0: return True
        if l1!= l2: return False
        if s1 == s2: return True
        if s1[0] == '(' and s2[0] == ')':
            return match(s1[1:], s2[1:])
        elif s1[0] == ')' and s2[0] == ')':
            return match(s1[1:], s2[1:])
        else:
            return False
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if match(lst[i], lst[j]): return 'Yes'
    return 'No'

