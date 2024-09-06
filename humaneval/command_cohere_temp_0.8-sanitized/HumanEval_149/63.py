def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    new_list = []
    for item in lst:
        if len(item) % 2 == 0:
            new_list.append(item)
    new_list.sort()
    return new_list