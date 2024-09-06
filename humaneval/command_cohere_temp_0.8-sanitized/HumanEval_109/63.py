def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # If there's a duplicate, it's impossible to sort
    if len(unique_arr) != len(sorted_arr):
        return False

    # Shift the elements to create a new array
    shifted_arr = [element for element in sorted_arr[1:]] + [sorted_arr[0]]

    # Check if the new array is sorted
    return move_one_ball(shifted_arr)