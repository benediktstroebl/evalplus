def sorted_list_sum(lst):
    lst_len = [len(i) for i in lst]
    lst_alpha = [i for i in lst if len(i) % 2 == 0]
    lst_alpha = sorted(lst_alpha, key=lambda x: (x, lst_len.index(len(x))))
    return lst_alpha