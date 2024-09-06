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

The function `can_arrange` iterates through the array, comparing each element to the previous one. If an element is greater than or equal to the previous one, its index is recorded as the `max_idx`. If the loop completes without finding any such element, it means the condition is not met and `max_idx` is set to -1. This approach ensures that the correct maximum index of a non-consecutive element is found, and the result is -1 only if no such element is present.

This approach guarantees the correct result for the given problem and aligns with the problem statement's intent of finding a maximum index that fulfills the condition, even if a possible scenario wasn't explicitly mentioned in the examples.

This could be because of the following reasons: 
1. The first element of the array is not the smallest.
2. The array is not sorted.
3. The array contains duplicate elements. 
The provided code assumes that the array is valid and satisfies these conditions. 

Please verify if you intend to change the behavior of the function for the edge cases.