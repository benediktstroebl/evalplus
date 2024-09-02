
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

    # O(n)
    if lst == []:
        return lst
    if len(lst) == 1:
        return lst

    small_num = min(lst)
    large_num = max(lst)

    # print(small_num)
    # print(large_num)

    # O(n)
    lst.remove(small_num)
    lst.remove(large_num)
    # print(lst)

    # O(1)
    lst_small = [small_num]
    lst_large = [large_num]

    # O(n)
    if len(lst) > 1:
        lst_small.append(min(lst))
        lst_large.append(max(lst))
    if len(lst) == 1:
        lst_small.append(lst[0])

    # O(n)
    for item in lst:
        if item < min(lst_small):
            lst_small.append(item)
        elif item > max(lst_large):
            lst_large.append(item)
        else:
            lst.remove(item)

    # O(n)
    lst_small.extend(lst_large)

    return lst_small
