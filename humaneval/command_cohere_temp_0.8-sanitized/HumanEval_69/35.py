def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > max_val:
            max_val = i 
        if i == max_val and lst.count(i) >= i:
            freq = i 
    return max_val if freq == -1 else -1