
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

    # to solve this problem, we'll need to do a bunch of checks
    # the first check is to see if there are any bad pairs in the string
    bad_pairs = 0
    for i, _ in enumerate(lst):
        if lst[i] == '(' and lst[i + 1] == ')':
            bad_pairs += 1
    if bad_pairs % 2!= 0:
        return 'No'

    # next, we'll check for the balance between open and close parens
    open_parens = 0
    close_parens = 0
    for i, _ in enumerate(lst):
        if lst[i] == '(':
            open_parens += 1
        elif lst[i] == ')':
            close_parens += 1

    # if there is an unbalanced number of parens, it is not good
    if open_parens!= close_parens:
        return 'No'

    # we are now ready to check for the first balanced parens
    open_index = -1
    for i, _ in enumerate(lst):
        if lst[i] == '(':
            open_index = i
        if lst[i] == ')':
            # if we find a balanced pair, we return the string
            if open_index < i:
                return 'Yes'
    return 'No'
