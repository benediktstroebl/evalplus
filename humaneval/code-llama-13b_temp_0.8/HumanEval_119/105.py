
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
    def parens_count(lst):
        count = {'(': 0, ')': 0}
        for paren in lst:
            count[paren] += 1
        return count
    left = 0
    right = 0
    for key in parens_count(lst).keys():
        if key == '(':
            left += parens_count(lst)[key]
        elif key == ')':
            right += parens_count(lst)[key]
    if left == right:
        return 'Yes'
    else:
        return 'No'

