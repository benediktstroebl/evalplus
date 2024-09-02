
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
    if lst == []:
        return []
    # the minimum value will always be the first element in the sorted list
    minimum = min(lst)
    # the max value will be the last element in the sorted list
    max_val = max(lst)
    # min_max_vals contains the min and max values
    min_max_vals = [minimum, max_val]
    # the result will be the length of the list + 1
    result = len(lst) + 1
    # for every integer in the list
    for number in lst:
        # if the integer is not the min or max
        if number!= minimum and number!= max_val:
            # get the index of the integer from min_max_vals
            min_max_vals.remove(number)
            # get the index of the integer in the list
            index = lst.index(number)
            # set the integer at the index to the min_max value
            lst[index] = min_max_vals[0]
            # set the min_max value to the index of the number in the list
            min_max_vals[0] = index
            result -= 1
    return lst
