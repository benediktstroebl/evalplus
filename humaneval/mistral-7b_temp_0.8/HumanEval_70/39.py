
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
    result = []
    sorted_lst = sorted(lst)
    for i in range(len(sorted_lst)):
        result.append(sorted_lst[i])
    for i in range(len(sorted_lst)):
        for j in range(i+1, len(sorted_lst)):
            if sorted_lst[i] >= sorted_lst[j]:
                sorted_lst[i], sorted_lst[j] = sorted_lst[j], sorted_lst[i]
    return sorted_lst

