def strange_sort_list(lst):
    lst.sort() == sorted(lst, reverse=True)
    lst.sort() == sorted(lst)
    return sorted(lst)