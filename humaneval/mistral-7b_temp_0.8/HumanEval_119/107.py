
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
    # list contains two strings. We need to concat them somehow.
    # how to check if the concated string is valid?
    # put all the parens into a stack
    # make a new string while popping out parens from the stack
    # if the new string contains less open parens than close parens, then it's invalid
    # return 'no' if invalid, else return 'yes'
    # Edge Cases:
    # one of the string is empty
    # both strings are empty
    # one of the strings is only ')'
    # both strings are only ')'
    if len(lst) == 1:
        if lst[0] == '':
            return 'Yes'
        elif ')' in lst[0]:
            return 'No'
    elif len(lst) == 2:
        if lst[0] == lst[1]:
            return 'Yes'
        elif ')' in lst[0] and ')' in lst[1]:
            return 'No'
        else:
            return 'Yes'
    elif len(lst) ==
