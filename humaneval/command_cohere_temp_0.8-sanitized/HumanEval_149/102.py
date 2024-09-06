def sorted_list_sum(lst):
    lst_new = []
    for string in lst:
        if len(string) % 2 == 0:
            lst_new.append(string)
    lst_new.sort()
    return lst_new