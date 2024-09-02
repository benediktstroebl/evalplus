
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
    # Convert the string into a list
    lst = list(map(list, lst))
    # If there are more closing than open, we know the string is bad
    if len(lst[0]) > len(lst[1]):
        return 'No'
    # If there are more open than close, we know the string is bad
    elif len(lst[0]) < len(lst[1]):
        return 'No'
    # If there are the same number of open and close, we know the string is good
    elif len(lst[0]) == len(lst[1]):
        return 'Yes'


















