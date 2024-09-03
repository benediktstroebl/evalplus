def largest_smallest_integers(lst):
    if len(lst) == 0:
        return (None, None)
        
    max_num = max(lst)
    min_num = min(lst)
    
    if max_num < 0:
        max_num = -max_num  # Swap to ensure positive

    return (max_num, min_num)