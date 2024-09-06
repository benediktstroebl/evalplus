
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

    # 0: Open, 1: Close
    stack = [0] * len(lst)
    open_parentheses_count = 0

    for i, char in enumerate(lst):
        if char == '(':
            open_parentheses_count += 1
            stack[i] = 0
        elif char == ')':
            if stack[i - 1] == 1:
                return 'No'

            open_parentheses_count -= 1
            if open_parentheses_count < 0:
                return 'No'

            stack[i] = 1

    if open_parentheses_count == 0:
        return 'Yes'

    return 'No'
