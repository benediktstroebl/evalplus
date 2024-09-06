def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)

    # Reduce the result by 1 if current element is repeated
    for i in range(len(arr)):
        if arr[i] == arr[i][::-1]:
            result -= 1

    return result