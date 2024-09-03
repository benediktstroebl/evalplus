def can_arrange(arr):
    # Initialize the largest index found so far with -1
    max_index = -1

    # Iterate through the array
    for index, element in enumerate(arr):
        # If the current element is larger than the element before it, find the largest index
        if element > arr[max_index]:
            max_index = index  # Update the maximum index

    # Return the largest index found
    return max_index
arr = [1,2,4,3,5]