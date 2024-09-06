def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort lst_result by the length of words, and if the length is the same, sort it alphabetically
    lst_result.sort(key=lambda x: (len(x), x))
    return lst_result