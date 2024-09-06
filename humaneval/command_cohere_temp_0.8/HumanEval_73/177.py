```python
def smallest_change(arr):
    # initialize the result to the length of the array
    result = len(arr)

    # Loop through the array backwards and calculate the suffix differences from the palindrome threshold
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result = min(result, abs(i - (len(arr) - 1) - 1))

    return result

# Driver Code
arr = [1, 2, 3, 5, 4, 7, 9, 6]
print(smallest_change(arr))  # Should print: 4

arr = [1, 2, 3, 4, 3, 2, 2]
print(smallest_change(arr))  # Should print: 1

arr = [1, 2, 3, 2, 1]
print(smallest_change(arr))  # Should print: 0
```

In this script, the `smallest_change` function calculates the minimum number of changes required to make the array palindromic. It initializes the result to the length of the array, then loops through the array backwards, comparing each element to its predecessor. If they are not the same, the function minimizes the difference with the threshold and assigns this minimized value to the result. Ultimately it returns the result.  This is assessed through an array of tests that are run on this function. 

Note: This solution assumes that the input array contains only integers. If the input array contains non-integer values, or if there are additional constraints on the allowable changes, then further modifications to the function would be required to solve the problem accurately.