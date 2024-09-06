def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    # sort by len() and alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst