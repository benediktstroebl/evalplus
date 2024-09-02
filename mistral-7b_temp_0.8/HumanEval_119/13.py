
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
    #Your code here.

    # '''
    # |-------------------------
    # | ()()
    # | )(
    # |
    # |
    # |()
    # | ()()
    # | )(
    # |
    # '''

    def match(s):
        '''
        Helper function to check if parentheses are matched in a string
        '''
        stk = []
        for c in s:
            if c == '(':
                stk.append(c)
            else:
                if stk and stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(c)
        return len(stk) == 0

    if match(lst[0]) and match(lst[1]):
        return 'Yes'
    return 'No'

