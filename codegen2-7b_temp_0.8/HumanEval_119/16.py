
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
    def check_parentheses(str_):
        open_parentheses, closed_parentheses = 0, 0
        for char in str_:
            if char == '(':
                open_parentheses += 1
            elif char == ')':
                closed_parentheses += 1
            if closed_parentheses < open_parentheses:
                return False
        return closed_parentheses == open_parentheses

    return 'Yes' if check_parentheses(lst[0]) and check_parentheses(lst[1])
    else:
        return 'No'

