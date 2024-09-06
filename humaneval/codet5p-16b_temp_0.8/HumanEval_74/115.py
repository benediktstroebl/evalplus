
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

    count1 = 0
    count2 = 0
    total_list = []

    for i in range(len(lst1)):
        count1 += len(lst1[i])
        count2 += len(lst2[i])

    if count1 > count2:
        for i in range(len(lst2)):
            total_list.append(lst2[i])
    elif count2 > count1:
        for i in range(len(lst1)):
            total_list.append(lst1[i])

    return total_list

