
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
    list_len = len(lst)
    if list_len == 0:
        return 'Yes'
    if list_len == 1:
        if lst[0] == '()':
            return 'Yes'
        else:
            return 'No'
    else:
        for i in range(0, list_len):
            for j in range(1, list_len):
                if len(lst[i]) == len(lst[j]):
                    if match_parens(lst[i:j]) == 'Yes':
                        if match_parens(lst[j:]) == 'Yes':
                            return 'Yes'
                    else:
                        return 'No'
        return 'No'
