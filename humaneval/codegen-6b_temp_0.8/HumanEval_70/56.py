
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
    # your code here
    if len(lst) == 0:
        return []
    else:
        min_value = min(lst)
        max_value = max(lst)
        temp = [x for x in lst if x == min_value]
        lst = [x for x in lst if x != min_value]
        temp.extend([x for x in lst if x == max_value])
        lst = [x for x in lst if x != max_value]
        temp.extend(lst)
        return temp

