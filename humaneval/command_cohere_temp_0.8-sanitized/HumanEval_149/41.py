def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    new_list = []
    for i in lst:
        if len(i) % 2 == 0:
            new_list.append(i)
    new_list.sort()
    return new_list