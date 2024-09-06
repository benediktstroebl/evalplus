
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
    #check if parenthesis are balanced
    def is_parens_balanced(str):
        #count the number of open and closed parenthesis
        opened = closed = 0
        for i in str:
            if i == '(':
                opened += 1
            else:
                closed += 1
            if closed > opened:
                return False
        return opened == closed
    if is_parens_balanced(lst[0]) and is_parens_balanced(lst[1]):
        return 'Yes'
    return 'No'
