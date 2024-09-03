def sorted_list_sum(lst):
    # remove strings with odd length
    lst = [sub for sub in lst if len(sub) <= 1]
    # sort list based on length of each word
    return sorted(lst, key=lambda x: len(x))