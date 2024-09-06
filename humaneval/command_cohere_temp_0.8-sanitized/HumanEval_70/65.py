def strange_sort_list(lst):
    """
    Do a strange sort of a list - return it in order of min, max, min, max,...
    """
    res = []
    while len(lst) > 1:
        res.append(min(lst))
        res.append(max(filter(lambda x: x != res[-1], lst)))
        lst = [x for x in lst if x != res[-1] and x != res[-2]]
    if lst:
        res.extend(lst)
    return res