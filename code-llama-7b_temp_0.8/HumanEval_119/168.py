
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
    # open_close = []
    # for paren in lst[0]:
    #     if paren == '(':
    #         open_close.append('(')
    #     else:
    #         if open_close and open_close[-1] == '(':
    #             open_close.pop()
    #         else:
    #             return 'No'
    # for paren in lst[1]:
    #     if paren == ')':
    #         open_close.append(')')
    #     else:
    #         if open_close and open_close[-1] == ')':
    #             open_close.pop()
    #         else:
    #             return 'No'
    # if open_close:
    #     return 'No'
    # else:
    #     return 'Yes'

    # Another solution
    # Count open and close parentheses
    # return 'No' if the sum of open and close parentheses is not 0
    # return 'Yes' otherwise
    cnt_op = lst[0].count('(')
    cnt_cl = lst[1].count(')')
    return 'No' if cnt_op + cnt_cl != 0 else 'Yes'

