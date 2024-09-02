
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''

    # A = ['hi', 'admin']
    # B = ['hI', 'Hi']
    # C = ['hi', 'hi', 'admin', 'project']
    # D = ['hI', 'hi', 'hi']
    # E = ['4']
    # F = ['1', '2', '3', '4', '5']

    # total_match(A, B) ➞ ['hI', 'Hi']
    # total_match(A, C) ➞ ['hi', 'admin']
    # total_match(D, A) ➞ ['hI', 'hi', 'hi']
    # total_match(E, F) ➞ ['4']

    total_lst1 = 0
    total_lst2 = 0

    for i in lst1:
        total_lst1 += len(i)

    for j in lst2:
        total_lst2 += len(j)

    if total_lst1 == total_lst2:
        return lst1
    elif total_lst1 < total_lst2:
        return lst1
    else:
        return lst2

