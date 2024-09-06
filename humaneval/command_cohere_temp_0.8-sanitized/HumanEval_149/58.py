def sorted_list_sum(lst):
    lst = [e for e in lst if len(e) % 2 == 0]
    # Sorting the list based on the length of words first, then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst