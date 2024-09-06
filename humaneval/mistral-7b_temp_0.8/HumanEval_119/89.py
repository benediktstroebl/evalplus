
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
    # --------
    return 'No' if ('(' in lst[0] and ')' in lst[0] and not '(' in lst[1]) or ('(' in lst[1] and ')' in lst[1] and not '(' in lst[0]) else 'Yes'
    # --------
    return 'No' if ('(' in lst[0] and ')' in lst[0] and not '(' in lst[1]) or ('(' in lst[1] and ')' in lst[1] and not '(' in lst[0]) else 'Yes'
    # --------
    return 'Yes' if '(' not in lst[0] or ')' not in lst[0] or '(' not in lst[1] or ')' not in lst[1] else 'No'
    # --------
    return 'No' if len([i for i in lst[0] if i in '(]') and len([i for i in lst[1] if i in '([')]) else 'Yes'
    # --------
    
