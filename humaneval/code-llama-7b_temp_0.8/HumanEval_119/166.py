
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
    def paren_match(sublst, count_open, count_closed):
        if len(sublst) == 0:
            return count_open == count_closed
        if sublst[0] == '(':
            return paren_match(sublst[1:], count_open+1, count_closed)
        return paren_match(sublst[1:], count_open, count_closed+1)

    lst1 = lst[0].replace(')', '(')
    lst2 = lst[1].replace(')', '(')
    return 'Yes' if paren_match(lst1 + lst2, 0, 0) else 'No'
