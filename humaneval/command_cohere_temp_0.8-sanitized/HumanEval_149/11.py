def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_length = len(str(lst[0]))
        new_list = []
        for i in lst:
            if len(i) == strings_length:
                new_list.append(i)
        new_list.sort()
        return new_list