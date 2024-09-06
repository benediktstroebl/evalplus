
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
    def matching(lst, first_half, second_half):
        while len(lst) > 0 and first_half and second_half:
            if lst[0] == '(':
                first_half.append(lst.pop(0))
            else:
                if not first_half:
                    return False
                first_half.pop()
                second_half.append(lst.pop(0))
        if first_half == [] and second_half == []:
            return True
        return False
    return 'Yes' if matching(lst, [], []) else 'No'

