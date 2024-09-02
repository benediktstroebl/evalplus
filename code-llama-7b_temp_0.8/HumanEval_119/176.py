
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
    # first, we need to count the number of '(' and ')' in lst
    # The sum of the two numbers must be equal
    lst_count = []
    for i in lst:
        lst_count.append(i.count('('))
        lst_count.append(i.count(')'))
    if sum(lst_count) % 2 == 0:
        return 'Yes'
    else:
        return 'No'

