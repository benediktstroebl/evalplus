
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
    length = 0
    for i in lst1:
        length += len(i)
    for i in lst2:
        length += len(i)

    if length == len(lst1):
        return lst1
    else:
        return lst2


    # time complexity: O(n), space complexity: O(n)
    lst_1 = []
    lst_2 = []
    for i in lst1:
        for j in lst2:
            if len(i) < len(j):
                lst_1.append(i)
            else:
                lst_2.append(j)

    if len(lst_1) == 0:
        return lst_2
    else:
        return lst_1
