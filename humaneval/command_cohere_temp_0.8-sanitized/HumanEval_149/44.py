def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    # Sorting the list in ascending order
    lst.sort(key=lambda x: (len(x), x))
    return lst