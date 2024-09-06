def strange_sort_list(lst):
    result = []
    while len(lst) > 0:
        minval = min(lst)
        maxval = max(x for x in lst if x > minval)
        result.extend([minval, maxval])
        lst = [x for x in lst if x != minval and x != maxval]
    return result