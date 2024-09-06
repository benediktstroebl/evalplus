def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > 0:
            freq = lst.count(i)
            if max_val < i and freq >= i:
                max_val = i 
            elif max_val >= i and freq < i:
                max_val = -1 
            if max_val > 0 and freq >= max_val: 
                return max_val 
        elif freq >= 0: 
            return -1 
    return -1