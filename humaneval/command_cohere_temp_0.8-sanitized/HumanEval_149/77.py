def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_len_list = []
        for s in lst:
            strings_len_list.append(len(s))
        strings_len_list.sort()
        temp = []
        for i in range(lst_length):
            temp.append(lst[strings_len_list.index(i)])
        return temp