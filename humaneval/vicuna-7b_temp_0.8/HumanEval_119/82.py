
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
    left = lst[0]
    right = lst[1]
    # If the left string has only one parenthesis
    if len(left) == 1:
        # If the right string has only one parenthesis
        if len(right) == 1:
            # if they match
            if right == '(' or right == ')':
                return 'Yes'
        # If they don't match
        else:
            return 'No'
    # If the left string has more than one parenthesis
    else:
        # If the right string has more than one parenthesis
        if len(right) > 1:
            # If they match
            if right == '(' or right == ')':
                return 'Yes'
        # If they don't match
        else:
            return 'No'

lst = [[')', '('], ['(', ')']]
result = match_parens(lst)
