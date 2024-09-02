
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
    # your code goes here
    a = lst[0]
    b = lst[1]
    # the idea here is to check if there are any parentheses that are not closed
    # we do this by getting the length of the number of parentheses that are
    # open and the number of parentheses that are closed
    # if the number of open parentheses is greater than the number of closed
    # parentheses, it is not possible to create a good string
    # because there will be parentheses that are not closed
    open = 0
    close = 0
    for i in range(len(a)):
        if a[i] == '(':
            open += 1
        elif a[i] == ')':
            close += 1
    if open < close:
        return 'No'

    # we check if the number of open parentheses is greater than or equal to the
    # number of closed parentheses
    # if it is not possible to create a good string with the two given strings,
    # it is possible to create a good string with the
