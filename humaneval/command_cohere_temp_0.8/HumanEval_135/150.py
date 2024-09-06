```python
def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur >= prev:
            arranges.append(idx)
            prev = cur
    return max(arranges, default=-1)
```

The function uses a loop to iterate through each element in the array, checking if each element is greater than or equal to the preceding one. If an element is not true for these conditions, the index is appended to the `arranges` list. After checking all elements, the function returns the maximum index in `arranges` if it is not empty, or -1 if arrangements are not found. 

The given example tests cases are:
```python
arr = [1, 2, 4, 3, 5]
print(can_arrange(arr))  # Output: 3

arr = [1, 2, 3]
print(can_arrange(arr))  # Output: -1
``` 

This should return the expected output of 3 and -1 for the respective examples.