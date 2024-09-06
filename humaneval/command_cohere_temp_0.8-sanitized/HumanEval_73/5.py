def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)

    # Loop through the array and reduce result if a pair is found
    for i in range(len(arr)-1):
        if arr[i] != arr[len(arr) - 1 - i]:
            result = min(result, 2)

    # Loop through the array and reduce result if a triple is found
    for i in range(len(arr)-2):
        if arr[i] != arr[len(arr) - 1 - i] and arr[i] != arr[len(arr) - 2 - i]:
            result = min(result, 3)

    # Check for consecutive duplicates
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            result = min(result, arr.count(arr[i])-1)

    return result