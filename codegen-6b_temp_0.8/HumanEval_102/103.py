
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # We'll use a binary search to find the number.
    
    # Make sure x is smaller than y. 
    if x >= y:
        return -1

    # Now we find the largest even integer in the range [x, y]
    # by using two pointers, left and right. 
    left = 1
    right = x
    
    # Move left to the right until we find an even integer.
    while left <= right:
        mid = (left + right) / 2
        if is_even(mid) == True:
            left = mid + 1
        else:
            right = mid - 1
    
    # Check if it's in the right range.
    if right >= x:
        return right
    else:
        return -1
        
        