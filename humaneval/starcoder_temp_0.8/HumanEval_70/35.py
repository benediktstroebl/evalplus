
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
    if len(lst) <= 1:
        return lst
    else:
        # 1. Get the minimum value
        min_val = min(lst)

        # 2. Get index of the minimum value
        index = lst.index(min_val)

        # 3. Get the maximum value of the remaining elements
        max_val = max(lst[index + 1:])

        # 4. Get index of the maximum value
        max_index = lst.index(max_val)

        # 5. Swap the min and max values
        lst[index], lst[max_index] = lst[max_index], lst[index]

        # 6. Get the rest of the elements
        remaining = lst[index + 1:]

        # 7. Recursive call
        return [min_val] + strange_sort_list(remaining)
