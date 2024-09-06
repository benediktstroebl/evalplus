
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
    lst1 = lst[0]
    lst2 = lst[1]

    if len(lst1) == 0 or len(lst2) == 0:
        return 'No'
    elif (len(lst1) % 2) != 0 or (len(lst2) % 2) != 0:
        return 'No'
    elif len(lst1) > len(lst2):
        lst1 = lst1[:len(lst2)] + lst1[len(lst2):]

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return 'No'
    return 'Yes'
