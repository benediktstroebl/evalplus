
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

    lst.sort()
    s = ''.join(lst)
    left, right = 0, len(s)-1
    while left<right:
        if s[left]=='(' and s[right]==')':
            left+=1
            right-=1
        elif s[left]==')' and s[right]=='(':
            left+=1
            right-=1
        else:
            return 'No'
    return 'Yes'
