
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
        return []

    # if min(lst) is the same as max(lst), we have a sorted list
    if lst[0] == lst[-1]:
        return lst

    min_value = min(lst)
    max_value = max(lst)
    min_index = lst.index(min_value)
    max_index = lst.index(max_value)

    # swap the min and max elements
    lst[0], lst[min_index] = lst[min_index], lst[0]
    lst[-1], lst[max_index] = lst[max_index], lst[-1]

    # sorted_lst = lst[min_index:max_index + 1] + lst[:min_index] + lst[max_index + 1:]
    # other_lst = lst[:min_index] + lst[max_index + 1:] + lst[min_index:max_index + 1]

    # if list is of length 1 or 2, we can just return the list
    if len(lst) <= 2:
        return lst

    # find the middle index of the list
    middle_index = len(lst)/2

    # lst[:middle_index] has all elements to the left of the middle of the list
    sorted_lst = lst[:middle_index]

    # lst[middle_index:] has all elements to the right of the middle of the list
    other_lst = lst[middle_index:]

    # first, sort the left side
    sorted_lst = strange_sort_list(sorted_lst)

    # second, sort the right side
    other_lst = strange_sort_list(other_lst)

    # merge the two sorted lists
    sorted_lst += other_lst

    return sorted_lst

