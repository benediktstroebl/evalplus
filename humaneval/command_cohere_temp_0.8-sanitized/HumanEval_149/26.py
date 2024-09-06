def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        odd_idx = [i for i, x in enumerate(lst) if len(x) % 2 == 1]
        remove_ords = [ord(c) for c in lst[odd_idx[0]]]
        for i in odd_idx[1:]:
            remove_ords = [x for x in remove_ords if x != ord(lst[i][0])]
        remove_ords = list(set(remove_ords))
        filtered_lst = [x for x in lst if x[0] not in remove_ords]
        filtered_lst.sort(key=lambda x: (len(x), x))
        return filtered_lst