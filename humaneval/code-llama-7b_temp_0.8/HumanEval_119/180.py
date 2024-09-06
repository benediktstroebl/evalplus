
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
    assert len(lst) == 2, 'Length of lst should be 2'

    def _match_parens(first_lst, second_lst, current_parens):
        if not first_lst and not second_lst:
            return 'Yes'

        if not first_lst:
            return 'No' if ')' in second_lst else _match_parens(second_lst[1:], [], current_parens + second_lst[:1])

        if not second_lst:
            return 'No' if '(' in first_lst else _match_parens(first_lst[1:], [], current_parens + first_lst[:1])

        if first_lst[0] == ')' and second_lst[0] == '(':
            return _match_parens(first_lst[1:], second_lst[1:], current_parens + first_lst[:1] + second_lst[:1])

        if first_lst[0] == '(' and second_lst[0] == ')':
            return 'No'

        return _match_parens(first_lst[1:], second_lst[1:], current_parens + first_lst[:1] + second_lst[:1])

    return _match_parens(lst[0], lst[1], [])
