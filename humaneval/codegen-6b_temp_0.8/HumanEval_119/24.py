
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
    left, right = 0, 0
    for c in lst[0]:
        if c == "(":
            left += 1
        else:
            if left:
                left -= 1
            else:
                return "No"
    for c in lst[1]:
        if c == ")":
            if left:
                left -= 1
            else:
                return "No"
        else:
            right += 1
    if left or right:
        return "No"
    return "Yes"

