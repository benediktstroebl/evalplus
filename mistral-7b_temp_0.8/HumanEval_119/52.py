
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

    def match_parens_helper(lst):
        # first check if there are 2 different types of parens
        # then check that parens are even
        if lst[0][0] != lst[1][0]:
            return False
        if lst[0].count('(') != lst[0].count(')'):
            return False
        if lst[1].count('(') != lst[1].count(')'):
            return False

        # make a new list of parens
        new_list = [lst[0]]
        for i in range(1, len(lst)):
            new_list.append(lst[i])

        # check if parens match
        check = 0
        for j in range(len(new_list)):
            if new_list[j] == '(':
                check += 1
            else:
                check -= 1
            if check < 0:
                return False
        return True

    if len(lst) > 2:
        return False
    else:
       
