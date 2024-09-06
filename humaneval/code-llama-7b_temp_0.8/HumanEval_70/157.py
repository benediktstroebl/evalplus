
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
    # check if list is empty
    if lst == []:
        return []
    else:
        #initialize empty list
        strange_list = []
        # find the minimum value in list
        min_value = min(lst)
        # append minimum value to strange list
        strange_list.append(min_value)
        # subtract list from minimum value to obtain remaining values
        remaining_values = lst[:lst.index(min_value)] + lst[lst.index(min_value)+1:]
        # find the maximum value in remaining values
        max_value = max(remaining_values)
        # append maximum value to strange list
        strange_list.append(max_value)
        # subtract remaining values from maximum value to obtain min values
        min_values = remaining_values[:remaining_values.index(max_value)] + remaining_values[remaining_values.index(max_value)+1:]
        # append min values to strange list
        strange_list = strange_list + min_values
        return strange_list
