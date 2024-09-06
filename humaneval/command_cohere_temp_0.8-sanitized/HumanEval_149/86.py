def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort the list using an already sorted list as a criterion
    lst_result.sort(key=lambda x: len(x), reverse=True)
    # if two words have the same length, sort the list alphabetically
    lst_result.sort()
    return lst_result