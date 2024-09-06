def sorted_list_sum(lst):
    lst_filtered = [x for x in lst if len(x) % 2 == 0]
    return sorted(lst_filtered, key=lambda x: (len(x), x))