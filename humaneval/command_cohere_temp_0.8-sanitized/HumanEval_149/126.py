def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el != '']
    lst = lst + ['']
    if lst[-1] == '':
        lst = lst[:-1]
    lst = [el for el in lst if el != '']
    lst.sort(key=len, reverse=True)
    lst.sort()
    return lst