
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

    lst = lst.copy()
    result = ''
    result_list = []
    good_strings = []
    for i in range(len(lst)):
        result += lst.pop()
        result_list.append(result)
        if lst == []:
            if match_parens(result_list) == 'Yes':
                good_strings.append(result)
            result_list.pop()
            result = ''
        lst = lst.copy()
    if len(good_strings) > 0:
        return 'Yes'
    else:
        return 'No'
