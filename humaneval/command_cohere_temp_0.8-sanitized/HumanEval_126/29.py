def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    
    for num, dup in dups.items():
        if dup > 1: 
            return False
    
    return lst == sorted(lst)