def strange_sort_list(lst):
    out = []
    n = len(lst)
    if n == 0:
        return lst
    min_val = min(lst)
    max_val = max(lst)
    for i in range(n):
        if lst[i] == min_val:
            out.append(min_val)
            max_val = max(max_val, lst[i+1:])
        if lst[i] == max_val:
            out.append(max_val)
            min_val = min(min_val, lst[i-1:])
        if i == n-1 or lst[i] != min_val or lst[i] != max_val:
            out.append(lst[i])
    return out