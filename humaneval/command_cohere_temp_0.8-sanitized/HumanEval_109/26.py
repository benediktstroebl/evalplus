def move_one_ball(arr):
    # If the array is empty, it's naturally sorted so return True
    if not arr:
        return True
    # Initialize variables to store the last element and the number of shifts
    last = arr[-1]
    shifts = 0
    for num in arr:
        if num < last:
            return False
        # Count shifts if the current element is greater than the last element
        if num > last:
            shifts += 1
        last = num
    # If the count of shifts is equal to the length of the array, it's sorted
    return shifts == len(arr)