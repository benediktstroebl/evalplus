
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
    # This is a better solution as it runs in constant time
    # It uses a counter to keep track of the number of open parens,
    # and returns the correct value when the counter is equal to zero
    count = 0
    for paren in lst:
        if paren == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return 'No'
    return 'Yes' if count == 0 else 'No'

