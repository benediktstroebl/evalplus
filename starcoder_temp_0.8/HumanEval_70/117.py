
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

    # The algorithm is like a merge sort but the merge part
    # is reversed (it's the same for odd and even length lists)
    min_index = 0
    max_index = len(lst) - 1
    odd_len = (len(lst) % 2 == 1)

    while min_index < max_index:
        # Keep sorting with odd length lists
        if odd_len:
            if lst[min_index] > lst[max_index]:
                lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
                max_index -= 1
            else:
                max_index -= 1
                min_index += 1
        # Keep sorting with even length lists
        else:
            if lst[min_index] > lst[max_index]:
                lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
            min_index += 1
            max_index -= 1

    return lst
