
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
    if settings.USE_DJANGO_TZ:
        if len(lst) == 0:
            return []
        else:
            # strange sort, because we are sorting by item[0],
            # so we are sorting by increasing value
            lst_new = sorted(lst, key=lambda x: x[0], reverse=False)
            # strange sort, because we are sorting by item[1],
            # so we are sorting by increasing value
            lst_new = sorted(lst_new, key=lambda x: x[1], reverse=False)
            return lst_new
    else:
        if len(lst) == 0:
            return []
        else:
            # strange sort, because we are sorting by item[0],
            # so we are sorting by increasing value
            lst_new = sorted(lst, key=lambda x: x[0], reverse=False)
            # strange sort, because we are sorting by item[1],
            # so we are sorting by increasing value
            lst_new = sorted(lst_new, key=lambda x: x[1], reverse=False)
            return lst_new

