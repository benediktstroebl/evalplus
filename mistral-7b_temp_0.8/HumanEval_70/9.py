
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
    # Write your code here.
    # Correctness is more important than efficiency,
    # so don't worry about the speed of the code.

    if lst == []:
        return []

    min_elem = lst[0]
    max_elem = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < min_elem:
            min_elem = lst[i]
        elif lst[i] > max_elem:
            max_elem = lst[i]

    min_lst = []
    max_lst = []
    for i in range(len(lst)):
        if lst[i] == max_elem:
            max_lst.append(lst[i])
        elif lst[i] == min_elem:
            min_lst.append(lst[i])
        else:
            continue

    return min_lst + max_lst + min_lst + max_lst
