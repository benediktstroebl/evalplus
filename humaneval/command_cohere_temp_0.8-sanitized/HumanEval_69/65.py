def search(lst):
    freq, max_val = -1, 0 
    for n in lst:
        if n > max_val:
            max_val = n 
        elif n == max_val and lst.count(n) >= n:
            freq = n 
    return max_val if freq == -1 else -1