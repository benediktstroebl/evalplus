def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_with_odd_length = [s for s in lst if len(s) % 2 == 1]
        return sorted(lst[:lst_length-len(strings_with_odd_length)]+strings_with_odd_length)