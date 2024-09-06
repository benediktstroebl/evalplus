
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
    # Your code here
    if len(lst) <= 1:
        return lst
    else:
        min_value = lst[0]
        new_list = [min_value]
        for i in lst:
            if i == min_value:
                max_value = max(lst)
                new_list.append(max_value)
                lst.remove(max_value)
                new_list.append(min_value)
                lst.remove(min_value)
            elif i > min_value and i < max_value:
                min_value = i
                new_list.append(min_value)
        return new_list





