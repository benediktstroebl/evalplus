
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
    first_lst = []
    second_lst = []
    for i in lst1:
        total = 0
        for j in i:
            total += len(j)
        first_lst.append(total)

    for i in lst2:
        total = 0
        for j in i:
            total += len(j)
        second_lst.append(total)
    
    if first_lst == second_lst:
        return lst1
    elif first_lst > second_lst:
        return lst1
    else:
        return lst2

