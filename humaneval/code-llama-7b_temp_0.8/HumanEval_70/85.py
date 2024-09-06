
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
    # step 1: handle edge cases
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    # step 2: construct an array to store the values
    result = []
    # step 3: loop through the input array, and add values to the result array
    while len(lst) > 0:
        # step 3.1: find the minimum value in the array
        min_value = lst[0]
        min_index = 0
        for i in range(len(lst)):
            if lst[i] < min_value:
                min_value = lst[i]
                min_index = i
        # step 3.2: add the minimum value to the result array
        result.append(min_value)
        # step 3.3: remove the minimum value from the input array
        lst.pop(min_index)
        # step 3.4: handle the case where the input array has odd number of values
        if len(lst) == 0:
            break
        # step 3.5: find the maximum value in the array
        max_value = lst[0]
        for i in range(len(lst)):
            if lst[i] > max_value:
                max_value = lst[i]
        # step 3.6: add the maximum value to the result array
        result.append(max_value)
        # step 3.7: remove the maximum value from the input array
        lst.pop(lst.index(max_value))
    return result

