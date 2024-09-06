def sorted_list_sum(lst):
    lst_new = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_new.append(el)
    # sort
    lst_new.sort(key=lambda x: (len(x), x))
    return lst_new