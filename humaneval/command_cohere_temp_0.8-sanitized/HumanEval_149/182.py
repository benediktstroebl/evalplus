def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        temp = lst.copy()
        temp.sort(key = lambda x: (-x.count('a'), x))
        return temp
    else:
        temp = [val for val in lst if len(val) % 2 == 0]
        temp.sort(key = lambda x: (-x.count('a'), x))
        return temp