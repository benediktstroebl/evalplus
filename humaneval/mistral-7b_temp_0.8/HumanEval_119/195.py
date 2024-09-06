
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
    # Your code here

    # if len(lst) > 2 or lst[0] != '(' or lst[-1] != ')' or (len(lst) == 2 and lst[0] != lst[1]):
    #     return 'No'

    # if len(lst) == 2:
    #     return 'Yes'

    # count = 0
    # for num in lst:
    #     if num == '(':
    #         count += 1
    #     elif num == ')':
    #         count -= 1

    # if count == 0:
    #     return 'Yes'
    # else:
    #     return 'No'

    # # return 'Yes' if len(lst) == 2 else 'No'

    # # for item in lst:
    # #     if item == '(':
    # #         count += 1
    # #     elif item == ')':
    # #         count -= 1

    # # if count == 0:
    # #    
