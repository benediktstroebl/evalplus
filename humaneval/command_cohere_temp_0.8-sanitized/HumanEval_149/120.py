def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        len_grouped = []
        temp = []
        for i in range(lst_len):
            temp.append(lst[i])
        for i in temp:
            if len(i) == len(temp[0]):
                len_grouped.append(i)
        len_grouped.sort()
        del temp
        del lst
        return len_grouped