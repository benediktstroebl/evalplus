
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
    tot_len1 = 0
    tot_len2 = 0

    for i in lst1:
        for j in i:
            tot_len1 += len(j)
    for i in lst2:
        for j in i:
            tot_len2 += len(j)

    if tot_len1 == tot_len2:
        return lst1
    elif tot_len1 < tot_len2:
        return lst1
    elif tot_len2 < tot_len1:
        return lst2

