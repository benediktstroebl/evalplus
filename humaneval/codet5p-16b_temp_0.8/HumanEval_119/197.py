
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

    def check_parens(s):
        '''
        check if all the parentheses in s are balanced.
        Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
        '''
        open_par = ['(', '{', '[']
        close_par = [')', '}', ']']
        stack = []
        for c in s:
            if c in open_par:
                stack.append(c)
            elif c in close_par:
                if not stack:
                    return 'No'
                top = stack.pop()
                if top == open_par[close_par.index(c)]:
                    continue
                else:
                    return 'No'
        if stack:
            return 'No'
        else:
            return 'Yes'

    for p in lst:
        if check_parens(p) == 'No':
            return 'No'
    return 'Yes'


