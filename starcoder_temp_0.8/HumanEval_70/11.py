
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    #create a list of tuples containing the value at that index with the value at that index as the key
    tuple_list = []
    for i in range(len(lst)):
        tuple_list.append((lst[i], i))
    #sort the tuples based on the key
    tuple_list.sort()
    #return a list of the values
    sorted_lst = []
    for tup in tuple_list:
        sorted_lst.append(tup[0])
    return sorted_lst
