def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    lst_new.sort()
    for x in lst_new:
        if x != lst_new[0]:
            break
    return lst_new[:len(lst_new) - 1]