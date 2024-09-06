def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        len_grouped = []
        for i in lst:
            if len(i) != lst_len / 2:
                continue
            len_grouped.append(i)
        len_grouped.sort()
        return len_grouped