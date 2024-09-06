def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    new_list = []
    for item in lst:
        if len(item) % 2 == 0:
            new_list.append(item)
    new_list.sort()
    return new_list