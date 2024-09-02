
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
    seen = set()
    valid = []
    if len(lst) == 1:
        return 'Yes'
    for i in range(len(lst)):
        num_to_add = len(lst) - 1 - i
        for j in lst[i]:
            if j == '(':
                valid.append(num_to_add)
            else:
                valid.pop()
            if len(valid) == 0:
                if len(lst) % 2 == 1:
                    return 'No'
                else:
                    valid = [j for j in range(len(lst))]
                    break
        seen.add(num_to_add)
    return 'Yes' if len(seen) == len(lst) else 'No'

