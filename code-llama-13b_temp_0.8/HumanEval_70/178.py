
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
    if len(lst) < 2:
        return lst
    else:
        new_lst = []
        min_lst = []
        max_lst = []
        for i in lst:
            if i == min(lst):
                new_lst.append(i)
                min_lst.append(i)
            else:
                max_lst.append(i)

        for j in range(0, len(lst), 2):
            if j+1 < len(lst):
                new_lst.insert(j+1, max(max_lst))
                max_lst.remove(max(max_lst))

            else:
                new_lst.insert(j+1, max(max_lst))
                max_lst.remove(max(max_lst))
                new_lst.insert(0, min(min_lst))
                min_lst.remove(min(min_lst))

        return new_lst

