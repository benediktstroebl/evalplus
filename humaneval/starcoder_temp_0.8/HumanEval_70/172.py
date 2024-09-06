
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

    # check if list is empty
    if len(lst) == 0:
        return lst

    # assign min to first value
    min = lst[0]
    # create a new list of values greater than min
    greater = [x for x in lst if x > min]
    # sort greater list
    greater.sort()
    # create a new list of values less than min
    less = [x for x in lst if x < min]
    # sort less list
    less.sort()

    # add min to greater list
    greater.insert(0, min)
    # add min to less list
    less.insert(0, min)

    # return result
    return greater + less
