def strange_sort_list(lst):
    lst.sort(key='{:02}')
    return lst