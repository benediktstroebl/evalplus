def strange_sort_list(lst):
    # sort the list to get the index of the minimum value
    min_index = sorted(range(len(lst)), key=lst.__getitem__)[0]
    # return the minimum value and exclude it from the list
    return [val for val in lst if val != lst[min_index]] + [lst[min_index]]