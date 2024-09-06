def sorted_list_sum(lst):
    lst_result = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_result.append(el)
    lst_result.sort()
    return lst_result