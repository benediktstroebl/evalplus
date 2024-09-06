```python
def can_arrange(arr):
    result = -1
    for idx, val in enumerate(arr):
        if arr[idx] > arr[idx - 1]:
            result = idx
            break
    return result
```

The function `can_arrange` loops through each index and value in the input array, checking whether the current element is greater than the previous one. If it encounters an element that isn't greater than the previous one, it assigns the current index to the `result` variable and breaks out of the loop. If no such index is found, the function assigns -1 to `result` instead.