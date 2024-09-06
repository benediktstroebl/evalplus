
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

    # 1st solution (0.81s)
    # open = 0
    # for el in lst:
    #     if el == '(':
    #         open += 1
    #     if el == ')' and open:
    #         open -= 1
    # return 'No' if open else 'Yes'

    # 2nd solution (0.09s)
    # a, b = lst
    # a = a.replace('(', '')
    # b = b.replace(')', '')
    # return 'No' if (len(a) != len(b)) else 'Yes'

    # 3rd solution (0.03s)
    return 'Yes' if ''.join(lst).count('(') == ''.join(lst).count(')') else 'No'
