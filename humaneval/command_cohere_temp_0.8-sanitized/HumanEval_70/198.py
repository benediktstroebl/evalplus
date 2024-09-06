def strange_sort_list(lst):
    # allocate the result list
    result = []

    # sort by first element, then by maximum, then by first element of remaining etc.
    for i in range(len(lst)):
        # add first element to result
        result.append(lst[i])
        # remove first element from list
        lst[i] = lst[len(lst) - 1]
        lst.remove(lst[len(lst) - 1])
    # if list is not empty, add remaining element to result
    if len(lst) != 0:
        result.append(lst[0])
    return result