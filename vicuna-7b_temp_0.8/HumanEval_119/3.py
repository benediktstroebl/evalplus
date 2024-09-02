
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
    # use a sliding window to check if all parens in the window are balanced
    n = len(lst)
    for i in range(n-1):
        j = i+1
        while j < n:
            if lst[i] == '(' and lst[j] in ['(', ')']:
                j += 1
            elif lst[j] == ')':
                if not lst[i-1] in ['(', ')']:
                    return 'No'
                j = i-1
            else:
                if lst[i] != lst[j]:
                    return 'No'
    return 'Yes'
