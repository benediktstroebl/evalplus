
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
    # return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    # lst = ['(', ')', ')', '(', '(']

    # a = ['(']
    # b = [')']
    # c = [')', ')', '(']

    a = [')']
    b = [')']
    c = ['(', '(']

    # lst = [')', '(', '(', '(', ')']
    # lst = ['(', '(', '(', ')', ')']
    # lst = ['(', '(', ')', ')', '(']
    # lst = ['(', ')', ')', '(', '(']

    # if (lst[0] == lst[1]):
    #     return 'Yes'
    # return 'No'

    # count = 0
    # for el in lst:
    #     if el == '(':
    #         count += 1
    #     elif el == ')':
    #         count -= 1
    # return 'Yes' if count == 0 else 'No'

    # for el in lst:
    #     if el == '(':
    #         a.append(el)
    #     else:
    #         if a and a[-1] == '(':
    #             a.pop()
    #         else:
    #             b.append(el)
    # return 'No' if b else 'Yes'

    # for el in lst:
    #     if el == '(':
    #         a.append(el)
    #     else:
    #         if a and a[-1] == '(':
    #             a.pop()
    #         else:
    #             b.append(el)
    # return 'No' if len(b) % 2 or a else 'Yes'

    # for el in lst:
    #     if el == '(':
    #         a.append(el)
    #     elif a and a[-1] == '(':
    #         a.pop()
    # return 'Yes' if not a else 'No'

    # a =
