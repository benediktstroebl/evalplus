
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

    
    def check_good(s):
        if len(s) == 0:
            return 'Yes'
        elif len(s) == 1:
            return 'No'
        else:
            i = 0
            while i < len(s):
                if s[i] == '(':
                    i += 1
                    if i == len(s):
                        return 'No'
                elif s[i] == ')':
                    i += 1
                    if i == len(s):
                        return 'No'
                else:
                    return 'No'
            return 'Yes'

    return check_good(lst[0]) + check_good(lst[1])
