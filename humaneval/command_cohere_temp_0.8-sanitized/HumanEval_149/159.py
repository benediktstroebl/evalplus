def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_len_list = []
        for string in lst:
            strings_len_list.append(len(string))
        strings_len_list.sort()
        filtered_list = [item for item in lst if item not in strings_len_list or strings_len_list.index(item) % 2 == 0]
        return filtered_list