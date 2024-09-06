
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_idx_sum = 0
    for idx in range(0, len(lst), 2):
        odd_idx_sum += lst[idx]
    return odd_idx_sum

