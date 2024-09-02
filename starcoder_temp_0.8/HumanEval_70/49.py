
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
    length = len(lst)
    if length == 1:
        return lst

    index = 0
    while index < length:
        val = lst[index]

        if val!= min(lst):
            # swap min with val
            lst.remove(min(lst))
            lst.append(val)

        else:
            # remove val
            lst.remove(val)

        length -= 1

    return lst
