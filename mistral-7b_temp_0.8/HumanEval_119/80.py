
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

    lst1 = list(lst[0])
    lst2 = list(lst[1])

    # The parentheses are balanced.
    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            if lst1[i] == ')' and lst2[i] == '(':
                return 'Yes'
        return 'No'

    # The length of the two parentheses are different.
    else:
        return 'No'
