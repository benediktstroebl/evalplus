
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
    # this is a disgusting solution but it works.
    # first, lets make a copy of the list,
    # then sort it, that way all of the close parens will be at the end
    # finally, we'll zip the sorted list and check it off as we go
    # if there's ever a close paren without an open paren, return 'No'
    # otherwise return 'Yes'
    lst = lst[:]
    lst.sort()
    for open_paren, close_paren in zip(lst, lst[::-1]):
        if open_paren == ')':
            return 'No'
    return 'Yes'
