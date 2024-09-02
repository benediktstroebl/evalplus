
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
    #your code here

    # 1. Convert string to list of chars and remove all non parens
    # 2. For each char in the left list, go through each char in the right list
    # 3. If a left char is an open paren, check if the next right char is a close paren.
    # 4. If the open paren in the left string matches the close paren in the right string, remove them both
    # 5. If the left list is empty, then we can concatenate these strings

    left = list(lst[0])
    right = list(lst[1])
    open_paren = '('
    close_paren = ')'

    # 1.
    for i in range(len(left)):
        if left[i] not in [open_paren, close_paren]:
            left.remove(left[i])
        if right[i] not in [open_paren, close_paren]:
            right.remove(right[i])

    # 2.
    for left_char in left:
        left_index
