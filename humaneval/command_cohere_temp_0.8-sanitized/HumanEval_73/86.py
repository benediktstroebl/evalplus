def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)

    # Consider all possible palindromic substrings and minimize the result
    for i in range(1, len(arr)):
        for j in range(i, len(arr)):
            # Take a copy of the array since we modify it in-place
            temp_arr = arr.copy()
            # Check if the subarray [arr[i], arr[j]] is a palindrome
            if temp_arr[i-1] == temp_arr[j]:
                # If it is, remove the characters at positions i and j, and recurse
                temp_arr.pop(i)
                temp_arr.pop(j)
                result = min(result, 1 + smallest_change(temp_arr))

    return result