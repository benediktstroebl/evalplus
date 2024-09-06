```python
def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            continue
        elif cur < prev:
            ans = idx
        else:
            prev = cur
    return ans if ans != len(arr) else -1
```

The function compares each element to the previous one, tracking the last index of the largest element that is not greater than its preceding element. If no such element is found, the function returns -1 to signify no suitable element. 

To improve efficiency, it is recommended to use Python's ` enumerate ` function for better code readability and to reduce the number of lines of code. The provided example above outlines the gist of the solution, and the following test cases can ensure that the function is operating correctly:
```python
test_cases = [
    ([1, 2, 4, 3, 5], 3),
    ([1, 2, 3], -1),
    ([1, 2, 2, 3, 4], 3),
    ([2, 3, 3, 5, 1], 1),
]

for arr, expected in test_cases:
    result = can_arrange(arr)
    assert result == expected, f"For array {arr}, expected {expected}, got {result}"
```

This approach allows for more efficient and concise problem-solving.