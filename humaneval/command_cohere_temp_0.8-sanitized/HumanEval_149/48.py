def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        temp = lst.copy()
        temp.sort()
        result = [i for i in temp if len(i) == int(lst_len / 2)]
        return result
    else:
        temp = lst.copy()
        temp.sort(key=lambda x: len(x))
        result = [i for i in temp if len(i) == int(lst_len / 2)]
        result.sort()
        return result