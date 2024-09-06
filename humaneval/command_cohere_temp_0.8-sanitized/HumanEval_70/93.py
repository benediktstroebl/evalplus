def strange_sort_list(lst):
    # Use dictionary to keep track of seen min and max values
    d = {}
    
    # Sorting and building result list at the same time
    result = []
    for v in lst:
        if v not in d:
            result.append(v)
        else:
            if len(d) == 1:
                result.append(d[-1])
            elif v > d[-2]:
                result.append(d[-1])
            else:
                result.append(d[-2])
            d[v] = v
    return result