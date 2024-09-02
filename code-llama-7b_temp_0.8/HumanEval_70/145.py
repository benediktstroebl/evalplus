
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
    #Create a list to return and initialize a variable to track the minimum
    result = []
    minimum = min(lst)
    #Find the minimum and maximum in the list and append them to the result
    while minimum in lst:
        lst.remove(minimum)
        result.append(minimum)
        maximum = max(lst)
        result.append(maximum)
        lst.remove(maximum)

    return result + lst
