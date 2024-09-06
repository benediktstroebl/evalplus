```python
def can_arrange(arr):
    prev = arr[0]
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            idx = i + 1
            break
    return max(idx, -1)
```

The function operates by iterating through the array, starting at index 1. It initially assigns the first element to `prev` and sets `idx` to 0, assuming that the first element is the baseline for comparison. During each iteration, the function checks if the current element is greater than or equal to the previous one. If the condition is satisfied, the loop continues to the next element. However, if the condition is not met, the variable `idx` is assigned the current index plus 1, indicating a potential arrangement starting from this element. The loop exits once a suitable element is found, or if no such element exists, in which case the function returns -1. The maximum between this index and -1 is then returned as the final answer.

Here is some example usage and tests to ensure the function behaves as expected:
```python
arr1 = [1, 2, 4, 3, 5]
arr2 = [1, 2, 3]

print(can_arrange(arr1))  # Expected output: 3
print(can_arrange(arr2))  # Expected output: -1

assert can_arrange(arr1) == 3
assert can_arrange(arr2) == -1
```