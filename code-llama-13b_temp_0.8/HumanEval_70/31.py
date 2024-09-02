
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
    if not lst:
        return lst

    sorted_lst = sorted(lst)
    odd_lst = []
    even_lst = []

    for idx, num in enumerate(sorted_lst):
        if idx % 2:
            odd_lst.append(num)
        else:
            even_lst.append(num)

    return [odd_lst[0], even_lst[0]] + odd_lst[1:] + even_lst[1:]

