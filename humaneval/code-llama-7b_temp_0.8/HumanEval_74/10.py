
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
    total = 0
    lst1_len = 0
    lst2_len = 0

    for i in range(0, len(lst1)):
        lst1_len += len(lst1[i])

    for j in range(0, len(lst2)):
        lst2_len += len(lst2[j])

    if lst1_len == lst2_len:
        return lst1
    elif lst1_len < lst2_len:
        return lst1
    else:
        return lst2
    
