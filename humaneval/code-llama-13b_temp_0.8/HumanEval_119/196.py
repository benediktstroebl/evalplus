
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

    def validate_parens(lst):
        count = 0
        for paren in lst:
            if paren == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    if len(lst) < 2:
        return 'No'
    lst1 = list(lst[0])
    lst2 = list(lst[1])
    if validate_parens(lst1):
        if validate_parens(lst2):
            return 'No'
        return 'Yes'
    if validate_parens(lst2):
        return 'No'
    lst1 = lst1 + lst2
    if validate_parens(lst1):
        return 'Yes'
    return 'No'

