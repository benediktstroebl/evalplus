def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        words = []
        for i in lst:
            if len(i) % 2 == 0:
                words.append(i)
        words.sort()
        return words