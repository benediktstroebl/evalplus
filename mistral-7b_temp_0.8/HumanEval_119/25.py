
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
    for l in lst:
        i = 0
        while i < len(l):
            if l[i] == '(':
                if i < len(l)-1:
                    if l[i+1] == ')':
                        l = l[0:i]+l[i+2:]
                        i -= 1
                    else:
                        return 'No'
                else:
                    return 'No'
            i += 1
    return 'Yes'
