
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
    # Wasn't able to solve the problem in time limit
    # Can't solve it in the given time limit
    # def check_valid(lst):
    #     for i in lst:
    #         if i == '(':
    #             lst.append(i)
    #         elif i == ')':
    #             lst.pop()
    #     return lst == []
    #
    # if check_valid(lst[0]) and check_valid(lst[1]):
    #     return 'Yes'
    # else:
    #     return 'No'

    # Didn't get the point of the exercise though
    # Trying to understand it
    # Why is this even the solution??
    # If lst == [('('), (')')] -> False
    # This is not even the solution
    # 1) First of all the solution expects a list of lists, not a list of strings.
    # 2) Second of all, it only checks if the first string is valid.
    # 3) Thirdly, it only checks if the first string is valid. It does not check
    # if the second string is valid.
    # 4) Lastly, what if the first string is invalid but the second string is
    # valid? The solution will return false when it should return true.
    # So the solution is not even correct.
    def check_valid(lst):
        for i in lst:
            if i == '(':
                lst.append(i)
            elif i == ')':
                lst.pop()
        return lst == []

    for i in range(len(lst)):
        lst[i] = list(lst[i])
    for i in range(len(lst[0])):
        for j in range(len(lst[1])):
            lst[0].insert(i+j, ')')
            lst[1].insert(i+j, '(')
            if check_valid(lst[0]) and check_valid(lst[1]):
                return 'Yes'
            lst[0].pop(i+j)
            lst[1].pop(i+j)
    return 'No'

