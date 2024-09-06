```python
def can_arrange(arr):
    prev = arr[0]
    max_idx = -1
    for idx, cur in enumerate(arr[1:]):
        if cur <= prev:
            max_idx = idx + 1
        prev = cur
    return max_idx
```

The function `can_arrange` uses a loop to iterate through the array, with the previous element stored in the `prev` variable. It increments the `max_idx` if the current element is less than or equal to the previous one. The loop continues until all elements have been checked against their predecessors. If no suitable element is found, `max_idx` remains -1. The provided example usages and test cases are good practices to ensure the function behaves as expected.  This algorithm has a time complexity of O(n) where n is the length of the input array.  This is efficient for this task as it only needs to iterate through the array once to find the maximum eligible index.