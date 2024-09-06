```python
def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[::-1]):
        if a != b:
            changes += 1
    return changes
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of changes required to make the array palindromic. The function uses a for loop to iterate through each pair of corresponding elements in the input array and its reverse. If the elements do not match, a count is kept track of through the variable `changes`. The final value of changes is returned, representing the least number of changes required to make the array palindromic. 

This algorithm has a time complexity of O(n^2) due to the n iterations in the for loop, where n is the length of the input array.