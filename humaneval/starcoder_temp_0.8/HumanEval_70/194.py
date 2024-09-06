
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
    if lst == []:
        return []
    min_value = min(lst)
    max_value = max(lst)
    strange = []

    # 1. First we need to sort the minimum value
    strange.append(min_value)

    # 2. Then we need to sort the maximum value
    strange.append(max_value)

    # 3. Then we need to sort the remaining integers
    lst.remove(max_value)
    lst.remove(min_value)
    strange.extend(lst)

    return strange

