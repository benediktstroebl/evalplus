def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if freq < n:
            freq = lst.count(n)
    return max_val if max_val >= freq else -1