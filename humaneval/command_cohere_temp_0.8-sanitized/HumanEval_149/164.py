def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    new_lst = [val for val in lst if len(val) % 2 == 0]
    new_lst.sort(key=lambda x: (-len(x), x))
    return new_lst