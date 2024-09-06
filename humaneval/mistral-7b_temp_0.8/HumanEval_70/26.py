
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
    # initialize an empty list
    ans = []
    # initialize a variable to store the smallest element
    smallest = None
    # loop through the list
    for i in range(len(lst)):
        # if the smallest element is not found, store the current element
        if smallest is None:
            smallest = lst[i]
        # if the smallest element is larger than the current element, store the current element
        elif lst[i] < smallest:
            smallest = lst[i]
    # add the smallest element to the end of the list
    ans.append(smallest)
    # remove the smallest element from the list
    lst.remove(smallest)
    # loop through the list again
    while len(lst) > 0:
        # store the maximum element in the list
        max = lst[0]
        # loop through the remaining elements and find the maximum
        for i in range(len(lst)):
            if lst[i] > max:
                max = lst[i]
        # add the maximum element to the list
        ans.append(max)
