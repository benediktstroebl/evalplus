
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
    def is_balance(s):
        '''
        Count the number of open and close parentheses for each pair of
        open and close parentheses in a string.
        '''
        open_paren, close_paren = 0, 0
        for i in s:
            if i == '(':
                open_paren += 1
            elif i == ')':
                close_paren += 1
        return open_paren == close_paren

    def make_string(lst, start_index):
        '''
        Take a list of strings as input, starting from position start_index,
        and return a new list of strings that concatenates them.
        '''
        if start_index == len(lst):
            return lst
        else:
            char = lst[start_index]
            if char == ')':
                lst[start_index] = '('
                return make_string(lst, start_index+1)
            elif char == '(':
                lst[start_index] = ')'
                return make_string(lst, start_index+1)
            else:
                return make_string(lst, start_index+1)

    def is_good_string(lst):
        '''
        Check if all parentheses in a given string are balanced.
        '''
        return len(lst) % 2 == 0 and is_balance(lst)

    def match_parens_helper(lst, index):
        '''
        Helper function for match_parens. Recursively finds the solution for a
        string using the given list of strings as input.
        '''
        if index == len(lst):
            return is_good_string(lst)

        char = lst[index]

        if char == '(':
            return match_parens_helper(lst, index+1)
        elif char == ')':
            return (not match_parens_helper(lst, index+1))

    return 'Yes' if match_parens_helper(list(lst[0]), 0) else 'No'
