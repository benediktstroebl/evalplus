
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

    def parens(s):
        open_p = 0
        for c in s:
            if c == '(':
                open_p += 1
            if c == ')':
                if open_p:
                    open_p -= 1
                else:
                    return False
        return open_p == 0

    return 'Yes' if parens(lst[0] + lst[1]) or parens(lst[1] + lst[0]) else 'No'

