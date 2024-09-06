
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
    # you can write your code here
    lst = list(lst)
    while True:
        min_index = lst.index(min(lst))
        min_value = lst[min_index]
        lst.remove(min_value)
        lst.insert(len(lst), min_value)
        if len(lst) == 0:
            return lst
        max_index = lst.index(max(lst))
        max_value = lst[max_index]
        lst.remove(max_value)
        lst.insert(len(lst), max_value)
