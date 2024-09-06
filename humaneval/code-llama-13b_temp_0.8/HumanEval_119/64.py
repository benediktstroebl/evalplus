
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
    # def check_balance(a, b):
    #     if a == 0 and b == 0:
    #         return True
    #     elif a > b:
    #         return check_balance(a - 1, b)
    #     elif b > a:
    #         return check_balance(a, b - 1)
    #     else:
    #         return False

    # a = lst[0].count('(')
    # b = lst[0].count(')')
    # if check_balance(a, b):
    #     a = lst[1].count('(')
    #     b = lst[1].count(')')
    #     if check_balance(a, b):
    #         return 'Yes'
    #     else:
    #         return 'No'
    # else:
    #     return 'No'

    return 'Yes' if abs(lst[0].count('(') - lst[0].count(')')) == abs(lst[1].count('(') - lst[1].count(')')) else 'No'
