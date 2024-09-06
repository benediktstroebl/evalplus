
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

    def is_balanced(parens_str):
        lparen_count = 0
        rparen_count = 0
        for p in parens_str:
            if p == '(':
                lparen_count += 1
            else:
                rparen_count += 1

            if lparen_count < rparen_count:
                return False

        return lparen_count == rparen_count

    if not is_balanced(lst[0]) or not is_balanced(lst[1]):
        return 'No'

    l1 = [p for p in lst[0]]
    l2 = [p for p in lst[1]]

    l = l1 + l2

    while True:
        if is_balanced(l):
            return 'Yes'
        for i in range(len(l)):
            l_new = l[:]
            if l_new[i] == '(':
                l_new[i] = ')'
            else:
                l_new[i] = '('
            l_new = l_new[:i+1] + l[i+1:]
            l = l_new
            break

        if l == l1 + l2:
            return 'No'

