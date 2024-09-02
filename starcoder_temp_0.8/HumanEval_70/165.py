
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

    m = min(lst)
    m_index = lst.index(m)
    lst_ = lst.copy()
    lst_.pop(m_index)
    lst_ = [m] + sorted(lst_) + [m]

    return lst_

