def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        temp = [elt for elt in lst if elt]
        temp.sort()
        return temp
    else:
        temp = [elt for elt in lst if len(elt) % 2 == 0]
        temp.sort()
        return temp