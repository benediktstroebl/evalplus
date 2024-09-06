
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

    list_length = len(lst)
    i = 0
    j = 0
    k = 0

    while i < list_length:
        if j > list_length-2:
            break
        if k > list_length-2:
            k = 0
        print(i)
        print(j)
        print(k)
        if lst[i] >= lst[k]:
            k += 1
        elif lst[i] <= lst[k] and lst[i] >= lst[j]:
            j += 1
        else:
            lst[i], lst[j] = lst[j], lst[i]
        i += 1

    return lst
