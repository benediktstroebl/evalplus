
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

    #return 'Yes' if both strings are empty or consist only of closing parentheses or both are empty and both strings are closed
    #if not all the parens are balanced
    #if not all the parens are balanced
    #in one string the parens are not closed
    #if not all the parens are balanced
    #if all parens are closed but the number of opening parens is not equal to the number of closing parens

    def is_balanced(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if count < 0:
                return False
        return True

    if lst == [] or lst == ['')] or lst == [''] or lst == [')']:
        return 'Yes'
    elif not is_balanced(lst[0]) or not is_balanced(lst[1]):
        return 'No'
    elif len(lst[0]) == 0 and len(lst[1]) ==
