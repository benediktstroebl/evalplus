def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        if val >= freq:
            freq = val 
    return max_val if max_val >= 0 and max_val >= freq else -1