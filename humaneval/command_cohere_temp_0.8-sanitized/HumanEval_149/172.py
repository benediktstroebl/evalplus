def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_len_list = []
        for string in lst:
            strings_len_list.append(string)
        strings_len_list.sort()
        temp = []
        for i in range(lst_length // 2):
            temp.append(strings_len_list[i])
        strings_len_list = temp
        return strings_len_list