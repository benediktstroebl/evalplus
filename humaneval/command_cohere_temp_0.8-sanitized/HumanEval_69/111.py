def search(lst):
    freq, max_val = 0, -1
    for n in lst:
        if n > max_val:
            max_val = n
        freq += 1
        if freq >= n:
            return n
    return -1