from collections import *
def pluck(arr):
    res, idx = None, None
    odds, evens = Counter(arr), Counter(filter(lambda x: x % 2 == 0, arr))
    
    if len(evens):
        res = min(k for k, v in sorted(evens.items()))
        idx = evens[res]
        return [res, idx] if idx < len(arr) else [res, -1]
    
    if len(odds):
        return [min(odds), idx_of_min(odds)]
    
    return []
def idx_of_min(counter):
    return min(range(len(counter)), key=lambda i: counter[i])