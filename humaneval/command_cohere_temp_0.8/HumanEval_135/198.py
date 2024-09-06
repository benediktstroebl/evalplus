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

The function `can_arrange` takes an array `arr` as input and returns the largest index of an element that is not greater than or equal to the element immediately preceding it. If no such element exists, it returns -1. The provided Python script defines the function using a loop to iterate through the array while tracking the previous element and returning the desired index. 

This approach allows you to efficiently determine the maximum index that satisfies the condition and seamlessly handles cases where no such element exists.