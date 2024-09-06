
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
    # 0 = open, 1 = closed, 2 = not used
    state = [2] * (2 * len(lst))
    for i, char in enumerate(lst):
        if char == '(':
            state[i] = 0
        elif char == ')':
            state[i] = 1
        else:
            assert False
    def match_parens_aux(i):
        if state[i] == 2:
            if match_parens_aux(i + 1):
                return True
            if match_parens_aux(i + 2):
                return True
        elif state[i] == 0 and state[i + 1] == 1:
            state[i] = state[i + 1] = 2
            return True
        return False
    if match_parens_aux(0):
        return 'Yes'
    return 'No'
