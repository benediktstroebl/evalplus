
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
    else:
        sorted_lst = [min(lst)]
        sorted_lst.extend(sorted(sorted_lst, key=lambda x: 1 if x < max(lst) else -1))
        return sorted_lst

