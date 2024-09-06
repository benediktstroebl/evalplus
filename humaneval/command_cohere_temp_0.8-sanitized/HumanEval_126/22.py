def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    
    for num in dups:
        if dups[num] > 1: 
            return False
    
    return lst == sorted(lst)