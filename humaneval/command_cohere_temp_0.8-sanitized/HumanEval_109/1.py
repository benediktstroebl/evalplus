def move_one_ball(arr):
    # Base case: If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Iterate through the array and count the number of elements that are greater than the last element
    count = sum(x > arr[-1] for x in arr)

    # If the count is greater than or equal to the length of the array, it's impossible to sort
    if count >= len(arr):
        return False

    # Otherwise, we can sort by shifting the last element to the front and removing one element from the count
    return move_one_ball(arr[:-1])