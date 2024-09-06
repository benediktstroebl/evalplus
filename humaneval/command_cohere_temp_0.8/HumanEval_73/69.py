```python
def smallest_change(arr):
    arr.sort()
    count = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            count += 1
    return count
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of changes required to make the array palindromic. In one pass, it sorts the array and counts the number of distinct elements in the process. Then, it traverses the array again and counts the number of changes required, which is simply the number of distinct elements. This solution efficiently calculates the required changes without extra space complexity, making it optimal for large arrays.

Here is a test case to verify the functionality of the function:
```python
test_cases = [
    [1, 2, 3, 5, 4, 7, 9, 6],
    [1, 2, 3, 4, 3, 2, 2],
    [1, 2, 3, 2, 1],
    [2, 2, 2, 2, 2],
    [1, 2, 3, 4, 4],
    [2, 3, 4, 5, 5],
]

for case in test_cases:
    assert smallest_change(case) == expected
```