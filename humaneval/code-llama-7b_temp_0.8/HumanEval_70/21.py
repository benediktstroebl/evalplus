
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
    result = []
    temp = []

    # Find Min, Max, and Remove
    for i in lst:
        if len(temp) == 0:
            min_value = max_value = i
            temp.append(i)
        else:
            if i > max_value:
                max_value = i
                temp.append(i)
            elif i < min_value:
                min_value = i
                temp.append(i)
            elif i == max_value:
                temp.append(i)
            elif i == min_value:
                temp.append(i)

    # Remove the Extras
    for i in temp:
        if i not in lst:
            lst.remove(i)

    # Add Min
    result.append(min_value)
    # Add Max
    result.append(max_value)
    # Add Min and Max
    for i in temp:
        if i not in lst:
            result.append(i)

    return result

    # TIME LIMIT EXCEEDED
    # for i in lst:
    #     if len(lst) == 1:
    #         return lst
    #     else:
    #         min_value = lst[0]
    #         max_value = lst[0]
    #         temp_list = []
    #
    #         for j in range(len(lst)):
    #             if lst[j] < min_value:
    #                 min_value = lst[j]
    #                 temp_list.append(min_value)
    #             elif lst[j] > max_value:
    #                 max_value = lst[j]
    #                 temp_list.append(max_value)
    #             else:
    #                 temp_list.append(lst[j])
    #
    #         for k in temp_list:
    #             if k in lst:
    #                 lst.remove(k)
    #
    #         result.append(min_value)
    #         result.append(max_value)
    #
    # return result

