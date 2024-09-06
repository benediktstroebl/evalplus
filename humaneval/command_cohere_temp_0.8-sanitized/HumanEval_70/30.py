def strange_sort_list(lst):
    # Create a copy of the list to avoid original modification
    result = lst[:]
    result.sort(key=lambda x: [x == min(lst), x == max(lst[:-1]), x])
    return result