
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
    total_lst = []
    for i in lst1:
        total = 0
        for k in i:
            total += ord(k)
        total_lst.append(total)
    for i in lst2:
        total = 0
        for k in i:
            total += ord(k)
        total_lst.append(total)
    return lst2 if lst1 == lst2 else lst1 if sum(total_lst[len(lst1):]) < sum(total_lst[:len(lst1)]) else lst1 if sum(total_lst[len(lst1):]) == sum(total_lst[:len(lst1)]) else lst2
