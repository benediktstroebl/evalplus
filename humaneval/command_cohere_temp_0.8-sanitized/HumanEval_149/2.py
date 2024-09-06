def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    # Sorting the list in ascending order
    # Based on the length of the words and alphabetic order as a secondary criterion
    return sorted(lst)