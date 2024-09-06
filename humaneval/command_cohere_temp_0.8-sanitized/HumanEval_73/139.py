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