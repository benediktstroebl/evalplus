from collections import *
def pluck(arr):
    # Your code here. 
    even_vals = defaultdict(list)
    
    for i, val in enumerate(arr):
        if val % 2 == 0:
            even_vals[val].append(i)
            
    if not even_vals:
        return []

    min_idx = min(idx for idx, _ in even_vals.values())
    return [min(even_vals), min_idx]