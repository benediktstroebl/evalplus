def strange_sort_list(lst):
    # Using only list comprehension and if statements
    # to create the strange sorting
    if lst:
        minval = min(lst)
        maxval = max(lst[1:])
        return [minval] + [maxval] * (len(lst) - 2) + [minval] * (len(lst) - 1)
    else:
        return []