
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

    # Input checks
    if not (type(lst) == list and len(lst) == 2 and isinstance(lst[0], str)
            and isinstance(lst[1], str)):
        return 'Input error'

    # Solving the problem
    count_left_par = 0
    count_right_par = 0
    lst_string = ''
    lst_string += lst[0]
    lst_string += lst[1]
    if lst_string == '()':
        return 'Yes'
    for letter in lst_string:
        if letter == '(':
            count_left_par += 1
        if letter == ')':
            count_right_par += 1
    if count_left_par == count_right_par:
        return 'Yes'
    else:
        return 'No'
