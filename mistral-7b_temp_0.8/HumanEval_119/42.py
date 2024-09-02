
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
    # if you can concat the 2 strings into 1 string and the resulting
    # string has the same number of opening parens as closing parens,
    # then it is a valid parens string.
    # i.e. if opening parens == closing parens, then it is valid
    # i.e. if you can make a good string, then you can say yes
    if len(lst[0]) == len(lst[1]):
        # if the lengths are the same, check for the parens balance
        # the first thing to check is if the number of opening parens
        # is equal to the number of closing parens
        if lst[0].count('(') == lst[1].count(')'):
            # if they are equal, then you can concatenate them
            # and return 'yes'
            return 'Yes'
        # if they are not equal, then you cannot concatenate them
        return 'No'
    # if the lengths of the 2 strings are not the same, then you cannot concatenate them
    return 'No'

