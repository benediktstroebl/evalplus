def strange_sort_list(lst):
    # Copy list to avoid altering the original list
    result = lst[:]
    result.sort(key=lambda x: [x == min(lst), x == max(lst), x])
    return result