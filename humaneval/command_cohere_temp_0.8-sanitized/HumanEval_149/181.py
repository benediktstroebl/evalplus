def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        new_lst = []
        for it in lst:
            if len(it) % 2 == 0:
                new_lst.append(it)
        new_lst.sort()
        return new_lst