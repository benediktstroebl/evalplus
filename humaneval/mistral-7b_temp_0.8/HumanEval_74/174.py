
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
    list1 = []
    list2 = []
    # print(len(lst1))
    for i in lst1:
        list1.append(sum(len(i) for i in lst1))
    # print(list1)
    for i in lst2:
        list2.append(sum(len(i) for i in lst2))
    # print(list2)

    if (sum(list1) > sum(list2)):
        return lst2
    else:
        return lst1
