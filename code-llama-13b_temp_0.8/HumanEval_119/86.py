
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
    # good = False
    # if lst[0] == ')' or lst[1] == '(':
    #     return 'No'
    #
    # for i in lst:
    #     if lst.count(i) % 2 != 0:
    #         return 'No'
    #
    # if len(lst) == 2:
    #     return 'Yes'
    #
    # else:
    #     if lst[0] == '(' and lst[1] == ')':
    #         lst = lst[1:]
    #         lst = lst[:-1]
    #         good = True
    #     else:
    #         good = False
    #
    #     if good == True:
    #         return match_parens(lst)
    #     else:
    #         return 'No'
    stack = []
    for p in lst:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) == 0:
                return 'No'
            stack.pop()
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'

