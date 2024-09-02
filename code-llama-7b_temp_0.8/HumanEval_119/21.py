
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
    # open: '(', ')'
    # close: ')'
    open = '('
    close = ')'
    # a list that keeps track of the number of open parentheses
    open_count = []
    for i in range(len(lst)):
        if lst[i] == open:
            open_count.append(i)
        else:
            if len(open_count) == 0:
                return 'No'
            else:
                index = open_count[-1]
                if lst[index] != open:
                    return 'No'
                else:
                    open_count.pop()
    if len(open_count) == 0:
        return 'Yes'
    else:
        return 'No'
