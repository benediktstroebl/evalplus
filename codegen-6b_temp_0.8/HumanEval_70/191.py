
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
    if len(lst) == 0:
        return []
    else:
        lst.sort()
        lst.reverse()
        lst.remove(lst[0])

        min_value = lst[0]
        max_value = lst[-1]

        ret = [min_value]

        for i in range(len(lst)):
            if lst[i] == min_value:
                for j in range(1, len(lst)):
                    if lst[j] > max_value:
                        lst[j], lst[j-1] = lst[j-1], lst[j]
                        ret.append(lst[j])
                        break
            elif lst[i] == max_value:
                ret.append(lst[i])
        return ret
