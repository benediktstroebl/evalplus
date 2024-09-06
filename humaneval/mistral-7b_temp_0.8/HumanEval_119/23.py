
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
    def is_good(s):
        '''Check if a string is balanced.'''
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
            else:
                i -= 1
        return i == 0
    return 'Yes' if is_good(lst[0]) and is_good(lst[1]) else 'No'

