
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
    string1 = lst[0]
    string2 = lst[1]

    open_par_count = 0
    close_par_count = 0

    for char in string1:
        if char == '(':
            open_par_count += 1
        else:
            close_par_count += 1

    for char in string2:
        if char == '(':
            open_par_count -= 1
        else:
            close_par_count -= 1

    if open_par_count == close_par_count:
        return 'Yes'
    else:
        return 'No'

