```python
def choose_num(x, y):
    max_even = -1
    for num in range(x, y + 1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even if max_even != -1 else -1

# Tests
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
```

This Python script defines a function `choose_num(x, y)` designed to find the largest even integer within the range between two given positive numbers `x` and `y`, and returns `-1` if no such number is found. The function iterates through the range from `x` to `y` (inclusive), checking if each number is even and updating the maximum even number found (`max_even`). The script includes a test module with two assertions: the first checks if the function correctly identifies the largest even number in the range (14) for the given inputs of 12 and 15, and the second verifies that the function returns `-1` when there is no even number in the range (13 and 12).  This succinct code efficiently addresses the problem statement and passes the provided tests.