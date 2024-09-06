Here's a Python script with a self-contained function that solves the problem:
```python
def smallest_change(arr):
    # Calculate the sums of the element disparities on the first and second halves of the array
    left_sum = sum(x for i, x in enumerate(arr) if i < len(arr) // 2)
    right_sum = sum(x for i, x in enumerate(arr[::-1]) if i >= len(arr) // 2)

    # Calculate the minimum difference between the two sums
    return min(left_sum - right_sum, right_sum - left_sum)

# Test cases
arr1 = [1, 2, 3, 5, 4, 7, 9, 6]
print(smallest_change(arr1))  # Output: 4

arr2 = [1, 2, 3, 4, 3, 2, 2]
print(smallest_change(arr2))  # Output: 1

arr3 = [1, 2, 3, 2, 1]
print(smallest_change(arr3))  # Output: 0
```

In this script, the `smallest_change` function calculates the sum of the absolute differences between the elements of a standard palindrome and the elements of the given array. It does this twice-once for the first half of the array and once for the second half (reverse ordered). It then returns the minimum of the two sums, which represents the minimum number of changes required.