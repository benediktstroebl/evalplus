
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
    # add whatever parameters you deem necessary - good luck!
    left = 0
    right = 0

    for i in range(len(lst[0])):
        if lst[0][i] == '(':
            left += 1
        elif lst[0][i] == ')':
            right += 1
        else:
            return "No"

    for i in range(len(lst[1])):
        if lst[1][i] == '(':
            left += 1
        elif lst[1][i] == ')':
            right += 1
        else:
            return "No"

    if left == right:
        return "Yes"
    else:
        return "No"

