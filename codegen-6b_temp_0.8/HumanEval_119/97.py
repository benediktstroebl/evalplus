
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
    from collections import deque
    bfs = deque([[lst[0], lst[1]]])
    visited = set()
    while bfs:
        lst, bfs = bfs, deque()
        i, j = lst[0], lst[1]
        s = i[0] + j[0]
        if s == '()' or s == '[]':
            return 'Yes'
        if lst[0] and lst[1] and s == '([' and s[-1] == ']':
            return 'No'
        for i in range(len(i)):
            if i > 0 and i < len(i) - 1:
                continue
            if i == 0:
                if len(j) > 1 or j[0][0] != '(' or j[0][-1] != ')':
                    continue
                lst.append([i, j[1:]])
            if i == len(i) - 1:
                if len(i) > 1 or i[0][0] != '(' or i[0][-1] != ')':
                    continue
                lst.append([i[1:], j])
            if i not in visited:
                visited.add(i)
                if j[0] != '(' or j[-1] != ')':
                    continue
                lst.append([i, j[1:]])
    return 'No'

