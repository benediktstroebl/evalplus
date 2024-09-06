def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_len_list = []
        for string in lst:
            if len(string) % 2 == 0:
                strings_len_list.append(string)
        strings_len_list.sort()
        return strings_len_list