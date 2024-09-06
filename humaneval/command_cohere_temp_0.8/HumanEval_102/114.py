```python
def choose_num(x, y):
    max_even = -1
    for i in range(x, y + 1):
        if i % 2 == 0 and i > max_even:
            max_even = i
    return max_even if max_even != -1 else -1

# Test Cases
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(2, 4) == 4
```

This Python script defines a function `choose_num(x, y)` designed to find the largest even integer within the range between two given positive numbers `x` and `y`, and returns `-1` if no such number exists. The function iterates through the range from `x` to `y` (inclusive), checking if each number is even and if it's larger than the current largest even number found, updating the max even number accordingly. Test cases are included to validate the function's behavior against specific examples, ensuring correct implementation.