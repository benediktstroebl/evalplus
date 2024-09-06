def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > 0:
            freq = lst.count(i)
            if freq >= i and (max_val < 0 or i > max_val):
                max_val = i 
    return max_val if max_val > 0 else -1