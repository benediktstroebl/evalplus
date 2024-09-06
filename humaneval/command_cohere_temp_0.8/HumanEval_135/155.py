```python
def can_arrange(arr):
    prev = arr[0]
    ans = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur <= prev:
            ans = idx
            prev = cur
    return ans
```

The algorithm works by first initializing the answer to be the first index of the first element (wrong assumption). Then it iterates over the array with a loop variable called `idx`, which is incremented each iteration. Meanwhile, `cur` handles the current element value and `prev` handles the previous point. It compares `cur` with `prev` and resets the answer if they're improperly ordered. If the elements are in order, it checks if the current index is the largest so far with the wrong assumption removed. Finally, the loop concludes with an index update if necessary before returning the answer. 

This approach ensures the correct solution is found and the highest index of the appropriately ordered element is returned, using an efficient single pass.