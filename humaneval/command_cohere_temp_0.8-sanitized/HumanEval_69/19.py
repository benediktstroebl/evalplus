def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if n >= freq:
            freq = n
    return -1 if max_val == 0 else max_val if freq >= max_val else -1