
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

    lst.sort()
    if len(lst) == 0:
        return 'Yes'
    if lst[0][0] == ')' or lst[-1][-1] == '(':
        return 'No'
    open_par_stack = []
    open_par_counter = 0
    for i in range(len(lst)):
        if lst[i][0] == '(':
            open_par_stack.append(lst[i])
            open_par_counter += 1
        else:
            open_par_stack.pop()
            open_par_counter -= 1
            if open_par_counter < 0:
                return 'No'
            if open_par_counter == 0:
                open_par_stack = []
                open_par_counter = 0
    return 'Yes'


