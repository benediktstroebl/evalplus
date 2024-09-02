
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
    # if lst is empty return empty list
    if not lst:
        return lst

    # create empty output list
    output = []
    # sort list
    lst.sort()

    # iterate over list to determine correct position
    for i in range(0, len(lst)):
        # get index of current element in list
        index = lst.index(i)
        # append next element to the output list
        output.append(lst[index+1])
        # append current element to the output list
        output.append(i)
    return output

