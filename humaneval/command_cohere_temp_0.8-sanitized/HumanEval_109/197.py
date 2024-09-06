def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize variables to store the last element and its index
    last_elem = arr[0]
    last_idx = 0
    # Iterate over the array to check if the desired permutation is possible
    for i in range(1, len(arr)):
        # If the current element is greater than the last element, it's impossible
        if arr[i] > last_elem:
            return False
        # If the current element is equal to the last element, update the index
        elif arr[i] == last_elem:
            last_idx = i
        # Update the last element and its index
        last_elem, last_idx = arr[i], i
    # If the last element is at its correct position, it's possible to sort
    return last_idx == 0