
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
    # start with empty string
    res = ''
    # check if first string is closed
    if lst[0] == ')':
        return res
    # check if second string is closed
    if lst[1] == ')':
        return res
    # check if there is a way to concatenate
    for i in range(2, len(lst)):
        # check if first string is open
        if lst[i] == '(':
            # check if res is closed
            if not res == ')':
                # add res to the end of the res
                res += lst[i]
                # check if res is closed
                if lst[i+1] == ')':
                    res += lst[i+2]
                    # check if res is closed
                    if lst[i+3] == ')':
                        return res
                    else:
                        # res is not closed
                        return 'No'
    # no way to concatenate
    return 'No'