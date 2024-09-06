```python
def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            arranged = i
            break
    return arranged
```

The function `can_arrange()` iterates through the array, comparing each element to the previous one. If an element is smaller than the previous one, the arrangement is possible, and the function returns the current index. If the loop completes without breaking, no arrangement is possible, and the function returns -1.

This solution allows you to quickly determine whether a sorted arrangement of the array is possible without explicitly sorting it. 

**NOTE:** The assumption of no duplicate values simplifies the problem and leads to this solution. Handling arrays with duplicates would require a different approach.