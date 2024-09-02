
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

    # 1. Check if list is empty
    if not lst:
        return []

    # 2. Create a list of even/odd indeces
    odd_idx = []
    even_idx = []
    for i in range(len(lst)):
        if i % 2:
            odd_idx.append(i)
        else:
            even_idx.append(i)

    # 3. Sort the list by selecting elements from the created lists
    new_lst = []
    while len(new_lst) < len(lst):
        # select from odd indeces
        if odd_idx:
            new_lst.append(lst[odd_idx.pop(0)])
        else:
            # select from even indeces
            new_lst.append(lst[even_idx.pop(0)])

    return new_lst

