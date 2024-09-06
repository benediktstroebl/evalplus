def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n:
                if n > max_val: max_val = n
    return -1 if max_val == 0 else max_val