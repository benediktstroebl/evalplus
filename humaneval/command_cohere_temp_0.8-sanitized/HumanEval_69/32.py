def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > 0:
            freq = lst.count(i)
            if max_val < freq:
                max_val = i 
    return -1 if max_val < freq else max_val