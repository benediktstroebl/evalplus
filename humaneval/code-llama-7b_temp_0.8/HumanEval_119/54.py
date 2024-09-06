
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
    # Your code goes here
    # if the length is not the same, there is no way to match
    if len(lst[0]) != len(lst[1]):
        return 'No'
    # if both strings are the same, there is no way to match
    if lst[0] == lst[1]:
        return 'No'
    # if both strings are empty, there is a way to match
    if lst[0] == '' and lst[1] == '':
        return 'Yes'
    # if the first string has more open parentheses, there is no way to match
    if lst[0].count('(') > lst[1].count(')'):
        return 'No'
    # if the first string has more close parentheses, there is no way to match
    if lst[0].count(')') > lst[1].count('('):
        return 'No'
    # if all the parentheses in the first string are open, there is a way to match
    if lst[0].count('(') == len(lst[0]):
        return 'Yes'
    # if all the parentheses in the first string are close, there is a way to match
    if lst[1].count(')') == len(lst[1]):
        return 'Yes'
    # if the first string ends with open parentheses, there is a way to match
    if lst[0][-1] == '(':
        return 'Yes'
    # if the first string ends with close parentheses, there is a way to match
    if lst[1][-1] == ')':
        return 'Yes'
    # if the first string ends with close parentheses but the next string does not
    # there is no way to match
    if lst[0][-1] == ')' and lst[1][-1] != ')':
        return 'No'
    # if the first string ends with open parentheses but the next string does not
    # there is no way to match
    if lst[0][-1] == '(' and lst[1][-1] != '(':
        return 'No'
    return 'Yes'

