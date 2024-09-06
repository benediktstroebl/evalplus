def sorted_list_sum(lst):
    lst = [str(ele) for ele in lst if len(ele) % 2 == 0]
    return sorted(lst, key=lambda x: (len(x), x))