
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

    # 1. list of parentheses is always even
    # 2. To check if list is valid, we must end with 0 open parentheses
    # 3. each open parenthesis must be closed at some point
    # 4. if string is valid, return Yes
    # 5. if string is not valid, return No

    # keep track of open parenthesis count
    count = 0
    # for each char in the string
    for char in lst:
        # if char is open parenthesis
        if char == '(':
            # increase count
            count += 1
        # otherwise, if char is close parenthesis
        elif char == ')':
            # decrease count
            count -= 1
            # if count is negative, return No
            if count < 0:
                return 'No'
    # if count is 0, return Yes
    if count == 0:
        return 'Yes'
    # otherwise, return No
    return 'No'

