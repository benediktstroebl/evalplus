
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

    # 1. check if first paren is '('
    # 2. if it is, recurse on the sublist of lst starting at index 1
    # 3. otherwise, if there's a matching paren in the second half of lst, recurse
    #    on the sublist starting at the index of the matching paren
    # 4. otherwise, return 'No'

    # O(n) time, O(n) space

    if len(lst) == 1:
        return 'Yes' if lst[0] == '(' else 'No'

    # check if first paren is '('
    if lst[0] == '(':
        return match_parens(lst[1:])
    else:
        # check if there's a matching paren in the second half of lst
        for i in range(int(len(lst) / 2)):
            if lst[i] == ')' and lst[-1 - i] == '(':
                return match_parens(lst[i+1:])

    return 'No'
