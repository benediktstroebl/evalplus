
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
    # q1 = deque(list(s1))
    # q2 = deque(list(s2))

    # deque_stack = []
    # while q1:
    #     if not q2:
    #         return 'No'
    #     if q1[0] == ')' and q2[0] == '(':
    #         q1.popleft()
    #         q2.popleft()
    #     elif q1[0] == ')' and q2[0] == ')':
    #         return 'No'
    #     elif q1[0] == '(' and q2[0] == '(':
    #         q1.popleft()
    #         q2.popleft()
    #     elif q1[0] == '(' and q2[0] == ')':
    #         return 'No'
    #     else:
    #         deque_stack.append(q1.popleft())
    #         deque_stack.append(q2.popleft())

    # while q2:
    #     if not q1:
    #         return 'No'
    #     if q1[0] == ')' and q2[0] == '(':
    #         return 'No'
    #     elif q1[0] == ')' and q2[0] == ')':
    #         return 'No'
    #     elif q1[0] == '(' and q2[0] == '(':
    #         return 'No'
    #     elif q1[0] == '(' and q2[0] == ')':
    #         return 'No'
    #     else:
    #         deque_stack.append(q1.popleft())
    #         deque_stack.append(q2.popleft())

    # print(deque_stack)
    # if not deque_stack:
    #     return 'Yes'

    # return 'No'

    stack, pair_stack = [], []
    for p in lst:
        if p == '(':
            stack.append