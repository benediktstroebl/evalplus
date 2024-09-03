def sorted_list_sum(lst):
    lst = list(filter(lambda x: len(x) <= 2, lst))
    return sorted(set(lst))