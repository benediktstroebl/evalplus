
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
    # How would you check if a string has balanced parentheses?
    # write a function to check the parens
    # then concat the strings and check if the string has balanced parens
    # keep track of left parens and right parens
    # keep track of the max right
    # if there is a left before a right
    # if the right is greater than the left return no
    # there should only be one left
    # there can be multiple right
    # return yes if the left is less than or equal to the right
    # return no otherwise
    # make sure the string is not empty
    # make sure there are only parens in the string
    # if there is a right paren before the left return no
    # else return yes

    def check_parens(string):
        # write a function to check if a string has balanced parens
        # keep track of left and right parens
        # keep track of the max right
        # if there is a left before a right
        # if the right is greater than the left return no
        # there should only be one left
        # there can be multiple right
        # return yes if the left is less than or equal to the right
        # return no otherwise
        # if there is a right before a left return False
        # if there is a right paren after a left paren return False
        # if there is a left paren after a right paren return False
        # return True
        left = 0
        right = 0
        max_right = 0
        for char in string:
            if char == '(':
                left += 1
            else:
                right += 1
            if right > left:
                return False
            if right > max_right:
                max_right = right
        if left <= max_right:
            return True
        return False

    # make sure the string is not empty
    if not lst[0] and not lst[1]:
        return 'No'
    # make sure there are only parens in the string
    if not all(char in '()' for char in lst[0] + lst[1]):
        return 'No'
    # if there is a right before
