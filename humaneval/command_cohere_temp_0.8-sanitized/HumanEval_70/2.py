def strange_sort_list(lst):
    # Sort the list, but always keep the minimum and maximum element in their respective places.
    # Then remove the sorted elements from the list, except for the minimum and maximum, and repeat until
    # the list is empty.
    return lst[:2].sort(key=lambda x: x[1:] if x[1:] else [x[0] + 1] + x[2:]) + lst[:2]