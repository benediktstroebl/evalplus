def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort the list alphabetically and by length
    lst_result.sort(key=lambda x: (len(x), x))
    return lst_result