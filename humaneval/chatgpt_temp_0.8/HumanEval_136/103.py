def largest_smallest_integers(lst):
    pos_ints = [i for i in lst if i > 0]
    neg_ints = [i for i in lst if i < 0]
    
    if not pos_ints:
        b = None
    else:
        b = min(pos_ints)
    
    if not neg_ints:
        a = None
    else:
        a = max(neg_ints)
    
    return (a, b)
