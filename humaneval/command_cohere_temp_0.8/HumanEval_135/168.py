```python
def can_arrange(arr):
    prev = arr[0]
    max_idx = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            max_idx = idx
            prev = cur
    return max_idx
```

The function `can_arrange` iterates through the array, comparing each element to the previous one. If an element is greater than or equal to the previous one, its index is recorded as a potential maximum. Finally, the function returns the highest index of all such elements or -1 if no such elements are found.

This approach assumes that the array has at least one element and uses the first element as the baseline for comparison, simplifying the logic required to find the threshold index. 

This implementation avoids duplicate elements and is efficient for larger arrays due to its iterative and progressive nature, making it more practical and scalable than a recursive approach.