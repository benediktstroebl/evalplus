```python
def smallest_change(arr):
    arr.sort()
    count = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            count += 1
    return count
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of changes required to make the array palindromic. In one pass, the function sorts the input array, then iterates through the array and counts the number of distinct elements. The number of distinct elements is the minimum number of changes required, which is then returned.

This algorithm's efficiency is `O(n log n)`, where `n` is the length of the input array. It is a linear time algorithm because it processes each element exactly once to determine the number of changes.

This code does not take any additional libraries, making it a self-contained Python script.