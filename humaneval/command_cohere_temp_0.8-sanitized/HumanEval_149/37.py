def sorted_list_sum(lst):
    lst_new = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_new.append(el)
    # sort function sorts strings alphabetically and numbers numerically
    return sorted(lst_new, key=str.lower)