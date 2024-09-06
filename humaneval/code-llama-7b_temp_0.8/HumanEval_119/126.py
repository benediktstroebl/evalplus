
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
    # pylint: disable=R1705
    lst_parens = lst[0] + lst[1]
    lst_parens_len = len(lst_parens)
    parens_count = 0
    for i in range(lst_parens_len):
        if lst_parens[i] == '(':
            parens_count += 1
        elif lst_parens[i] == ')':
            parens_count -= 1
            if parens_count < 0:
                return 'No'
    if parens_count == 0:
        return 'Yes'
    return 'No'
