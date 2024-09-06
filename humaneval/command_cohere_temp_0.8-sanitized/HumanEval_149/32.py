def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        odd_length_list = [x for x in lst if len(x) % 2 == 1]
        return sorted(lst[:lst_length-len(odd_length_list)]+odd_length_list)