
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

    def find_pair(lst, index, open_count):
        if index == len(lst):
            if open_count == 0:
                return True
            else:
                return False
        if lst[index] == '(':
            open_count += 1
        else:
            open_count -= 1
        return find_pair(lst, index + 1, open_count)

    def find_pair_in(lst, index, open_count):
        if index == len(lst):
            if open_count == 0:
                return True
            else:
                return False
        if lst[index] == '(':
            open_count += 1
        else:
            open_count -= 1
        if find_pair_in(lst[index + 1:], 0, open_count):
            return True
        return find_pair_in(lst, index + 1, open_count)

    # Check if both string are paren pairs
    if len(lst) % 2 != 0:
        return 'No'
    if find_pair(lst, 0, 0):
        return 'Yes'

    # Check if any single string is paren pairs
    left_lst = lst[0: len(lst) // 2]
    right_lst = lst[len(lst) // 2:]
    if find_pair(left_lst, 0, 0):
        return 'Yes' if find_pair_in(right_lst, 0, 0) else 'No'
    if find_pair(right_lst, 0, 0):
        return 'Yes' if find_pair_in(left_lst, 0, 0) else 'No'
    return 'No'
