def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > max_val:
            max_val = i 
        if i >= freq:
            freq = i
    return max_val if freq >= max_val else -1