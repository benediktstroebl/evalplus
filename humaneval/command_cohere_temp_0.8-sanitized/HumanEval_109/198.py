import random
def move_one_ball(arr):
    n = len(arr)
    # We make the first element the last element which will make the 
    # element at index 0 and all subsequent indices greater than the element 
    # at index n-1 which is what we want.
    arr[:] = [val for val in arr[n-1:-1] + arr[:n-1]]
    return arr == sorted(arr)