
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
    # your code here
    def check_balanced(s):
        # return True if s is balanced
        # return False otherwise
        if len(s) == 0:
            return True
        elif s[0] == '(':
            return check_balanced(s[1:])
        elif s[0] == ')':
            if len(s) == 1:
                return True
            return check_balanced(s[1:]) and check_balanced(s[:len(s)-1])
    if check_balanced(lst[0]) and check_balanced(lst[1]):
        return 'Yes'
    else:
        return 'No'
    # ---------------------------------------------------------------





















































































