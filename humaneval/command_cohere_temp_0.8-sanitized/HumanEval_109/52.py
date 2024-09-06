import random
def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    # Sort the array and get the index of the max element which is not at the last index.
    arr.sort()
    idx = arr.index(max(arr))
    # Shuffle the array in reverse order and get the index of the max element.
    random.shuffle(arr[:n-1][::-1])
    new_idx = arr.index(max(arr[:n-1][::-1]))[n-1]
    # If new_idx is smaller than idx, it is possible to get a non-decreasing array.
    return new_idx < idx