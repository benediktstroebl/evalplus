def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n:
                max_val = max(max_val, n)
        if freq > 0 and max_val >= 0:
            return max_val
    return -1