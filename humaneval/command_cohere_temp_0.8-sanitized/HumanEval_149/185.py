def sorted_list_sum(lst):
    lst = [e for e in lst if len(e) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst