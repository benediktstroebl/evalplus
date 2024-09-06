
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
    # first, you need to make sure you can concatenate the two strings.
    # check to make sure the last character of the first string is a ')'.
    # check to make sure the first character of the second string is a '('.
    # now you have something that looks like '(())'
    # go through the entire string, and check to make sure each '(' is followed
    # by a ')' and vice versa.
    # if you have any unmatched parentheses, return 'no'.
    # else, return 'yes'

    if lst[0][-1] != ')' or lst[1][0] != '(':
        return 'No'

    count = 0
    for i in lst[0]:
        if i == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return 'No'

    return 'Yes'

