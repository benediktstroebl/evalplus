
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
    
    total_list = []
    lst1 = lst1.copy()
    lst2 = lst2.copy()
    lst1.sort(key = len)
    lst2.sort(key = len)
    for i in lst1:
        for j in lst2:
            if len(j) < len(i):
                total_list.append(j)
            else:
                total_list.append(i)
                break
    return total_list
