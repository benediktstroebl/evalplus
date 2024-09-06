```python
def can_arrange(arr):
    prev = arr[0]
    mx = arr[0]
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > mx:
            mx = cur
        elif cur < prev:
            return idx
        prev = cur
    return -1 if mx == arr[-1] else idx
```
The `can_arrange` function iterates through the array, keeping track of the maximum element thus far (`mx`) and the previous element (`prev`). It returns the index of the first occurrence of `mx` or proceeds to the next iteration. If a smaller element (`cur`) is encountered compared to the previous element (`prev`), it returns the current index (`idx`). If the maximum element is the last element in the array, this means there are no smaller elements after it, indicating that no valid arrangement exists, so it returns -1. The provided example tests in the code demonstrate how the function works with different input arrays.