def next_smallest(lst):
    if len(lst) < 2:
        return None
    mn = min(lst)
    sm = sorted(lst)
    index = 0
    if sm[index+1] == mn:
        return sm[index+1]
    else:
        return None