
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
    if isinstance(lst, str) or isinstance(lst, str):
        open_lst = [s[0] for s in lst]
        close_lst = [s[1] for s in lst]
        # Find the first element in open_lst without matching an element in
        # close_lst.
        if open_lst[0] == '(' and close_lst[0] == ')':
            lst_len = len(lst)
            pair_lst = [0 for _ in range(lst_len)]
            for i in range(lst_len):
                if open_lst[i] == '(' and close_lst[i] == ')':
                    pair_lst[i] = 1
            # After filling in pair_lst, we check if there is a 1 in
            # pair_lst, that means there would be an unbalanced open bracket or
            # a balanced parenthesis error.
            if pair_lst.count(1) == 0:
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'
    return 'No'

