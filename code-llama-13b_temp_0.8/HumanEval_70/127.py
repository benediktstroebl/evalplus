
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
    # 1st solution
    n = len(lst)
    if n == 0:
        return lst
    new_lst = []
    n = 1
    while n <= len(lst):
        # find minimum in list
        min_value = min(lst)
        # find index of minimum in list
        ind_min = lst.index(min_value)
        # append index of minimum to new list
        new_lst.append(lst[ind_min])
        # remove min_value from list
        lst.remove(min_value)
        # find maximum in list
        max_value = max(lst)
        # find index of maximum in list
        ind_max = lst.index(max_value)
        # append index of maximum to new list
        new_lst.append(lst[ind_max])
        # remove max_value from list
        lst.remove(max_value)
        # if list is empty, break loop
        if lst == []:
            break
        # increment counter
        n += 1
    return new_lst

    # 2nd solution
    n = len(lst)
    if n == 0:
        return lst
    new_lst = []
    n = 1
    while n <= len(lst):
        # find minimum in list
        min_value = min(lst)
        # find index of minimum in list
        ind_min = lst.index(min_value)
        # append index of minimum to new list
        new_lst.append(lst[ind_min])
        # remove min_value from list
        del lst[ind_min]
        # find maximum in list
        max_value = max(lst)
        # find index of maximum in list
        ind_max = lst.index(max_value)
        # append index of maximum to new list
        new_lst.append(lst[ind_max])
        # remove max_value from list
        del lst[ind_max]
        # if list is empty, break loop
        if lst == []:
            break
        # increment counter
        n += 1
    return new_lst

    # 3rd solution
    
