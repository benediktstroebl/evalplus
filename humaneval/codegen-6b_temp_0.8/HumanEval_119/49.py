
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
    def is_next_balanced(lst, index, left_count, right_count):
        if index == len(lst):
            return True
        elif lst[index] == '(':
            left_count += 1
            right_count -= 1
            if not is_next_balanced(lst, index + 1, left_count, right_count):
                return False
        elif lst[index] == ')':
            right_count -= 1
            if not is_next_balanced(lst, index + 1, left_count, right_count):
                return False
        return True
    return 'Yes' if is_next_balanced(lst, 0, 0, 0) else 'No'
