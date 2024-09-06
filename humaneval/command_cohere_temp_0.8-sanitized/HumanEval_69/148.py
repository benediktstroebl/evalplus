def search(lst):
    freq, max_val = -1, 0
    for i in lst:
        if i > 0:
            max_val = i if i > max_val else max_val
            if i == freq:
                return i
            freq = lst.count(i)
    return -1