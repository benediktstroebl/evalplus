
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
    #shortest_list = min(len(lst1), len(lst2))
    #shortest_str = min(lst1, lst2)

    #return shortest_str

    total_list = []
    for i in lst1:
        total_list.append(len(i))
    total_list.sort()
    #print(total_list)
    min_list = total_list[0]

    min_list2 = []
    for i in lst2:
        min_list2.append(len(i))
    min_list2.sort()
    #print(min_list2)
    max_list = min_list2[0]

    if min_list == max_list:
        return lst1
    else:
        return lst2

