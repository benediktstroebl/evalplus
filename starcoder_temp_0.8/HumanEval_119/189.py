
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
    # O(n) time, O(1) space
    open_cnt = 0
    for char in lst:
        if char == '(':
            open_cnt += 1
        elif char == ')':
            open_cnt -= 1

        if open_cnt < 0:
            return 'No'
    return 'Yes' if open_cnt == 0 else 'No'
