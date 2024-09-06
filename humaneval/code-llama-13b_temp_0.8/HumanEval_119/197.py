
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
    def is_good(paren_list):
        count = 0
        for paren in paren_list:
            if paren == '(':
                count += 1
            else:
                count -= 1

            if count < 0:
                return False
        return True

    if len(lst) == 1:
        return 'Yes' if lst[0] == '()' else 'No'

    if len(lst) == 2:
        return 'Yes' if lst == ['(', ')'] or lst == ['()', '()'] else 'No'

    if is_good(lst):
        return 'Yes'

    for i in range(len(lst)):
        # permutation
        result = match_parens(lst[:i] + lst[i+1:])
        if result != 'No':
            return result

    return 'No'



