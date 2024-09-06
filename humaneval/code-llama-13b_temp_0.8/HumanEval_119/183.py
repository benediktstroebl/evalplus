
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

    # # my first idea was:
    # tmp = []
    # for x, y in zip(lst[0], lst[1]):
    #     if x == ')' and y == '(':
    #         tmp.append(')(')
    #     else:
    #         tmp.append(x)
    #     if len(tmp) > 0 and tmp[-1] == '(' and tmp[0] == ')':
    #         return 'No'
    #     elif len(tmp) > 0 and tmp[-1] == ')' and tmp[0] == '(':
    #         return 'No'
    # if len(tmp) == 0:
    #     return 'No'
    # else:
    #     return 'Yes'

    # my second idea was:
    # tmp = []
    # for x in lst[0]:
    #     if x == '(':
    #         tmp.append(x)
    #     else:
    #         if len(tmp) > 0:
    #             tmp.pop()
    #         else:
    #             return 'No'
    # for x in lst[1]:
    #     if x == ')':
    #         tmp.append(x)
    #     else:
    #         if len(tmp) > 0:
    #             tmp.pop()
    #         else:
    #             return 'No'
    # if len(tmp) == 0:
    #     return 'Yes'
    # else:
    #     return 'No'

    # my third idea was:
    # tmp = []
    # for x, y in zip(lst[0], lst[1]):
    #     if x == '(' and y == ')':
    #         tmp.append(x + y)
    #     elif x == ')' and y == '(':
    #         return 'No'
    #     elif x == '(' and y == '(':
    #         tmp.append(x)
    #     elif x == ')' and y == ')':
    #         tmp.append(y)
    #     else:
    #
