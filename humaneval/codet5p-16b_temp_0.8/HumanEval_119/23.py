
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

    def match(S):
        if len(S) % 2 == 1:
            return 'No'
        stk = []
        for char in S:
            if char == ')':
                if not stk:
                    return 'No'
                elif stk[-1] == '(':
                    stk.pop()
                else:
                    return 'No'
            else:
                stk.append(char)
        if stk:
            return 'No'
        else:
            return 'Yes'
    return match(lst[0]) + '\n' + match(lst[1])

