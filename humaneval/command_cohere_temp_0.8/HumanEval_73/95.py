Here's a Python script with a self-contained function that solves the problem:
```python
def smallest_change(arr):
    # Calculate lengths and differences
    n = len(arr)
    half = n // 2
    backwards_diff = [arr[i] - arr[n-1-i] for i in range(n)]
    # Calculate cumulative sum of absolute differences
    abs_diff_sum = sum(backwards_diff)
    for i in range(1, n):
        abs_diff_sum += abs(backwards_diff[i] - backwards_diff[i-1])
    # Calculate minimum changes
    min_changes = abs_diff_sum - half * (half + 1)
    # Handle edge case of single element
    if n == 1:
        return 0
    # Handle case of list of two elements
    if n == 2:
        return 1 if arr[0] != arr[1] else 0
    # Return minimum changes after determining the base case
    return min(min_changes, n - min_changes)
```

The function employs a few steps to determine the minimum changes:
1. It calculates the length of the array and its middle, as well as the absolute differences between corresponding elements when the array is read backwards.
2. It calculates the cumulative sum of absolute differences, which helps determine how many elements need to be changed to make the array palindromic.
3. It calculates minChanges using the cumulative sum and the theoretical maximum changes needed for a palindromic array.
4. It handles edge cases of single- and double-element arrays.
5. Finally, it returns the minimum number of changes, taking into account the base case of changing all elements.