def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        temp = lst.copy()
        temp.sort(key = lambda x: (-x.count('a'), x))
        return temp
    else:
        temp = [x for x in lst if len(x) % 2 == 0]
        temp.sort(key = lambda x: (-x.count('a'), x))
        return temp