
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
    # return 'Yes' if the condition is met or 'No' if not
    open_par = '('
    close_par = ')'
    lst_one = lst[0]
    lst_two = lst[1]
    lst_one_len = len(lst_one)
    lst_two_len = len(lst_two)

    if lst_one_len == 0:
        return 'Yes'

    if lst_two_len == 0:
        return 'Yes'

    if lst_one[lst_one_len-1] != lst_two[0]:
        return 'No'

    if lst_two[lst_two_len-1] != lst_one[0]:
        return 'No'

    if lst_one_len > lst_two_len:
        sub_list = lst_one[1:]
        for x in sub_list:
            if x == open_par:
                return 'No'
    if l
