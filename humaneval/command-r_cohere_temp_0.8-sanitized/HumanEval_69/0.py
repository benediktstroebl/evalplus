def search(lst):
    '''
    Returns the greatest integer with frequency >= the integer itself or -1 if none exist.
    '''
    if not lst:
        return -1
    
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    max_num = -1
    for num, count in freq.items():
        if count >= num:
            max_num = max(max_num, num)
    
    return max_num