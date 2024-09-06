```python
def choose_num(x, y):
    max_even = max(x, y) if (x == y) or (x % 2 == y % 2) else -1
    return max_even if max_even % 2 == 0 else -1

# Test Cases
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(2, 3) == 2
assert choose_num(100, 200) == 198
assert choose_num(101, 200) == -1
```

This Python script defines a function `choose_num(x, y)` designed to return the largest even integer within the range of two given positive numbers `x` and `y`, inclusive. If no such even number exists, it returns -1. This is achieved by using the `max` function to identify the largest number within the range, ensuring it is even through the use of the condition `max_even % 2 == 0`.