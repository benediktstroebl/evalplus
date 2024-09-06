def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_len_list = [len(word) for word in lst]
        strings_len_list = sorted(strings_len_list)
        sorted_list = [word for word in lst if len(word) in strings_len_list]
        return sorted_list