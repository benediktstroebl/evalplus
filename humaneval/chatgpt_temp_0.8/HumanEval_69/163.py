def search(lst):
    max_val = -1
    for val in set(lst):
        freq = lst.count(val)
        if val > 0 and freq >= val:
            max_val = max(max_val, val)
    return max_val
