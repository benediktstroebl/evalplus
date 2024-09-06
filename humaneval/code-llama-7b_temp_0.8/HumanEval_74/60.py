
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
    # length = []
    # for i in lst1:
    #     length.append(len(i))
    # for i in lst2:
    #     length.append(len(i))
    # length.sort()
    # return lst1 if length[0] < length[1] else lst2

    total1 = sum(len(i) for i in lst1)
    total2 = sum(len(i) for i in lst2)
    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1
