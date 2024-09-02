
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
    # return True if both strings are empty and balanced.
    if not lst[0] and not lst[1]:
        return 'Yes'
    # if lst[0] is empty but lst[1] is not, it means there's just one left
    # unbalanced open bracket, so you only need to match the last bracket,
    # and the string can be concatenated.
    elif not lst[0] and lst[1]:
        return 'Yes' if match_parens([lst[1][:-1]]) == 'Yes' else 'No'
    elif lst[0] and not lst[1]:
        return 'Yes' if match_parens(lst[0][1:]) == 'Yes' else 'No'
    else:
        # there are both open and close brackets in the two strings, need to
        # match them in pairs
        # always pick up the top left bracket pair for the first string
        lst1 = lst[0][1:]
        lst2 = lst[1][:-1]
        if match_parens([lst1, lst2]) == 'Yes':
            return 'Yes'
        else:
            return match_parens([lst1, lst2])

