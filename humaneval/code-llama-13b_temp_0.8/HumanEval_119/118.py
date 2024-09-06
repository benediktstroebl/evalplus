
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

    def check_parens(lst):
        counter = 0
        for paren in lst:
            if paren == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    def concat_and_check(first, second):
        return check_parens(first + second)

    if len(lst) == 1:
        return 'No' if lst[0] == ')' else 'Yes'
    if len(lst) == 2:
        return 'Yes' if concat_and_check(lst[0], lst[1]) else 'No'

    first, second, third = lst[0], lst[1], lst[2]
    # first + third + second
    # third + first + second
    # first + second + third
    if not concat_and_check(first, third):
        return 'No'
    return 'Yes' if concat_and_check(third + second, first) or concat_and_check(first + second, third) or concat_and_check(first, second + third) else 'No'

