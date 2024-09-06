```python
def smallest_change(arr):
    changed = 0
    for a, b in zip(arr, arr[1:][::-1]):
        if a != b:
            changed += 1
    return changed
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of changes required to make the array palindromic. The function uses a for loop to iterate through each pair of corresponding elements in the input array and its reverse. If the elements do not match, a change is counted. Finally, the total count of changes is returned to provide the minimum number of changes required to make the array palindromic. 

This algorithm has a time complexity of O(n^2) due to the nested loop, which iterates through the two arrays ('arr' and its reverse).