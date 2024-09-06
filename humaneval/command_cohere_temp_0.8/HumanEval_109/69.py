Here's a Python script that includes a function named `move_one_ball` optimized to solve the problem:
```python
def move_one_ball(arr):
    n = len(arr)
    arr.sort()
    expected = [0] * n
    expected[0] = arr[-1]
    expected[-1] = arr[0]
    for i in range(1, n):
        expected[i] = expected[i - 1]
    return expected == arr
```
This function initially sorts the array, then restores the initial order by assigning expected values at the appropriate positions. Finally, it compares the modified array with the expected values to determine if a non-decreasing order is possible.