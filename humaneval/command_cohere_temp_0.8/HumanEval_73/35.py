```python
def smallest_change(arr):
    arr.sort()
    count = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            count += 1
    return count
```

The function `smallest_change()` takes an array `arr` as input and returns the minimum number of changes required to make the array palindromic. In one change, you can change one element to any other element. The function sorts the input array and then counts the number of distinct elements in the sorted array as the changes parameter indicates that each change represents the transformation of one element to any other distinct element. Therefore, the number of distinct elements equals the number of changes required to make the array palindromic. The function returns the count.