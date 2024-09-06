
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

    total_lst1 = []
    total_lst2 = []
    for item in lst1:
        total_lst1.append(len(item))
    for item in lst2:
        total_lst2.append(len(item))
    if sum(total_lst1) == sum(total_lst2):
        return lst1
    elif sum(total_lst1) > sum(total_lst2):
        return lst2
    else:
        return lst1

