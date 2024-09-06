def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    # sort by length, and in case of a tie, by alphabetical order
    lst_new.sort(key=lambda x: (len(x), x))
    return lst_new