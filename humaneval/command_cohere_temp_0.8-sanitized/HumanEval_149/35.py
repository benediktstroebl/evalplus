def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        len_group = []
        temp = []
        for i in range(0, lst_len):
            if len(lst[i]) > 1 and lst[i][0] == lst[i][-1]:
                temp.append(lst[i][0])
            else:
                temp.append(lst[i])
        len_group = sorted(temp, key=len)
        return sorted(len_group)