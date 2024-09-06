def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        strings = []
        for string in lst:
            if len(string) % 2 == 0:
                strings.append(string)
        strings.sort()
        return strings