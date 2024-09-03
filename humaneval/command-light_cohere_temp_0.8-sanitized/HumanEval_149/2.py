def sorted_list_sum(lst):
    # remove strings with odd length
    lst = [sub for sub in lst if len(sub) == len(set(sub))]
    # sort the list by word length
    lst.sort(key=lambda x: x[0])
    return sorted(lst)