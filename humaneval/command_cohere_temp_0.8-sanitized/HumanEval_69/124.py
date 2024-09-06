def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        if val == max_val and lst.count(val) >= val:
            freq = val 
    return max_val if freq >= 0 else -1