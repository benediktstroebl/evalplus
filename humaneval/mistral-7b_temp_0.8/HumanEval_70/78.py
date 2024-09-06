
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
    # Write your solution here
    min_num = min(lst)
    max_num = max(lst)
    new_lst = []
    for num in lst:
        if num == min_num:
            new_lst.append(num)
        if num == max_num:
            new_lst.append(num)
    for num in range(min_num + 1, max_num):
        if num in lst:
            new_lst.append(num)
    return new_lst
