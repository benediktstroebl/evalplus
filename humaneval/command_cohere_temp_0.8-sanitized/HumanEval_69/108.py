def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            max_val = max(max_val, n)
            freq = lst.count(n)
        if freq >= n:
            return n
        if freq > max_val:
            max_val, freq = max_val, freq
    return -1