def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            max_val = max(max_val, n)
            if n >= freq:
                freq = n
    return max_val if freq >= max_val else -1