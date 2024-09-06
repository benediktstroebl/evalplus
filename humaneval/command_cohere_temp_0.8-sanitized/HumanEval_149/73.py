def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        temp = sorted(lst)
        temp.sort(key=lambda x: (len(x), x))
        return temp
    else:
        temp = [x for x in lst if len(x) % 2 == 0]
        temp.sort(key=lambda x: (len(x), x))
        return temp