```python
def smallest_change(arr):
    # Initialize the result to the maximum possible value to minimize it
    result = len(arr)

    for i in range(len(arr) // 2):
        left, right = arr[i], arr[-1 - i]
        if left != right:
            # Compute the minimum number of changes needed to make the array palindromic
            result = min(result, abs(i - (len(arr) - 1 - i))) + 1

    return result

# Test the function with some examples
assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
```

This script defines a function `smallest_change` that takes in an array `arr` as input and calculates the minimum number of elements that need to be changed to make the array palindromic. The function loops through the middle elements of the array, comparing each pair of elements. It calculates the minimum number of changes required to make the array palindromic for each pair and keeps the smallest value so far as the result. The provided assert statements test the function on the examples given in the problem statement.