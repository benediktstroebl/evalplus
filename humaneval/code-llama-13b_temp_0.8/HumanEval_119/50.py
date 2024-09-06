
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
    # if len(lst) == 1:
    #     return 'No'
    # print(lst)
    # if lst[0] == '(' and lst[1] == '(':
    #     lst[1] = lst[1] + lst[0]
    #     lst = lst[1:]
    #     return match_parens(lst)
    # if lst[0] == ')' and lst[1] == ')':
    #     lst[1] = lst[1] + lst[0]
    #     lst = lst[1:]
    #     return match_parens(lst)
    # if lst[0] == '(' and lst[1] == ')':
    #     lst[1] = lst[1] + lst[0]
    #     lst = lst[1:]
    #     return match_parens(lst)
    # else:
    #     lst[1] = lst[0] + lst[1]
    #     lst = lst[1:]
    #     return match_parens(lst)

    # def valid_brackets(par):
    #     count = 0
    #     for b in par:
    #         if b == '(':
    #             count += 1
    #         elif b == ')':
    #             count -= 1
    #         if count < 0:
    #             return False
    #     return count == 0

    # if len(lst) % 2 != 0:
    #     return 'No'
    # new_lst = lst[0] + lst[1]
    # if valid_brackets(new_lst):
    #     return 'Yes'
    # else:
    #     return 'No'

    if len(lst) % 2 != 0:
        return 'No'
    # print(lst)
    if lst[0] == '(' and lst[1] == ')':
        lst[1] = lst[1] + lst[0]
        lst = lst[1:]
        return match_parens(lst)
    elif lst[0] == '(' and lst[1] == '(':
