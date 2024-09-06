def sorted_list_sum(lst):
    lst_result = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_result.append(x)
    # sort by the length of words. In case of the same length, sort alphabetically
    lst_result.sort(key=lambda x: (len(x), x))
    return lst_result