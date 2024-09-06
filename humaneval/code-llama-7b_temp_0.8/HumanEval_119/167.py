
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
    d = {')': '(', '(': ')' }
    def check(s):
        stk = []
        for i in s:
            if i not in d:
                stk.append(i)
            elif len(stk) == 0 or stk.pop() != d[i]:
                return False
        return len(stk) == 0
    return 'Yes' if check(lst[0] + lst[1]) else 'No'

