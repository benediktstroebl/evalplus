def strange_sort_list(lst):
    # Algorithm:
    # 1. Sort the list in decreasing order (max to min)
    # 2. Remove the first element (now min) from the list
    # 3. Repeat steps 2 & 3 until the list is empty
    return [x for x in lst if not lst]