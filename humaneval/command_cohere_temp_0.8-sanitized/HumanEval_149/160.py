def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el != '']
    sorted_str = sorted(lst)
    # sort deletes duplicates, sort by length and then alphabetically
    sorted_str.sort(key=lambda x: (len(x), x))
    return sorted_str