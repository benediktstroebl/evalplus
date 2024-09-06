
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
    # first we'll split the string by parentheses and remove the first and last empty string
    lst = [i.split('(') for i in lst[1:-1]]
    # now we can check if the list contains all open parentheses
    # if yes, then we can just concatenate the lists
    # if not, then we can concatenate the lists and add the parentheses to the beginning and end of the list
    return lst if all(i[0] == '(' for i in lst) else 'No'
