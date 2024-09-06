def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > 0:
            max_val = i if i > max_val else max_val 
            if i == max_val and lst.count(i) >= i:
                freq = i 
    return -1 if max_val == 0 else freq