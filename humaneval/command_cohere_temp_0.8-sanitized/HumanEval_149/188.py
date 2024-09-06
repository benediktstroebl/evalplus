def sorted_list_sum(lst):
    lst_result = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_result.append(x)
    # sort the list using the built-in sort function
    lst_result = sorted(lst_result)
    return lst_result