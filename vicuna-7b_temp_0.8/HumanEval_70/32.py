
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
    # To get the largest number in the list
    max_num = max(lst)
    # To get the smallest number in the list
    min_num = min(lst)

    # Start with the smallest number
    result = [min_num]

    # Now we need to find the maximum number
    max_num_index = 0
    max_num_value = max_num
    for num in lst:
        if num > max_num:
            max_num = num
            max_num_index = i

    # Add the maximum number to the result
    result.append(max_num)

    # Now we need to find the smallest number
    min_num_index = max_num_index + 1
    min_num_value = min_num
    for num in lst:
        if num < min_num:
            min_num = num
            min_num_index = i

    # Add the smallest number to the result
    result.append(min_num)

    # Repeat the process until all numbers have been added to the result
    while len(lst) > 0:
        # Get the next smallest number
        num = lst.pop(0)
        # Add the next number to the result
        result.append(lst.pop(0))

    return result
