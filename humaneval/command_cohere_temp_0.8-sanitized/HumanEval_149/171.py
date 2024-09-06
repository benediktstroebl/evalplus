def sorted_list_sum(lst):
    lst_new = []
    for string in lst:
        if len(string) % 2 == 0:
            lst_new.append(string)
    # sort list alphabetically and by length of words - (lambda word): sorting key
    lst_new.sort(key=lambda x: (x, len(x)))
    return lst_new