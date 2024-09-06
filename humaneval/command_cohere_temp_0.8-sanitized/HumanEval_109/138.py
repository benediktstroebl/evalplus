def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array in place using sorting indices
    sorting_indices = [abs(arr.index(x)) for x in sorted(arr)]
    
    # If all sorting indices are even, it's possible to achieve non-decreasing order
    return all(x % 2 == 0 for x in sorting_indices)