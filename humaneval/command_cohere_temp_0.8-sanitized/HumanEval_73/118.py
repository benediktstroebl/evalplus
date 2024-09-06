def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)
    
    # Check if the array itself is a palindrome
    if arr == arr[::-1]:
        return 0
    
    for i in range(len(arr)):
        # Try to find a mirror index for each element
        j = len(arr) - i - 1
        # If the element is not the same as its mirror, subtract 1 from the result
        if arr[i] != arr[j]:
            result -= 1
            # If the element and its mirror are equal, we have found a palindrome and the result is the smaller of the two
            if arr[i] == arr[j] and result > 0:
                result = 0
            # If the element and its mirror are equal multiple times, we keep subtracting 1 until we reach the palindrome
            while i + 1 < len(arr) and j + 1 < len(arr) and arr[i + 1] == arr[j + 1]:
                result -= 1
                i += 1
                j += 1
                
    return result