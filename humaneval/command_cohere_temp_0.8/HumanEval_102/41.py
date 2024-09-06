```python
def choose_num(x, y):
    max_even = -1
    bounds = [x, y]
    for num in range(x, y + 1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even if max_even != -1 else -1

# Tests
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
```

This Python script defines the `choose_num` function, which takes two positive numbers `x` and `y` as input and returns the largest even integer that falls within the range `[x, y]`. The function initializes `max_even` to -1 and then iterates through the range from `x` to `y` (inclusive). For each number in this range, it checks if the number is even and if it's larger than the current `max_even`. If it passes both conditions, it updates `max_even`. Finally, the function returns `max_even` if it was updated successfully, or -1 if no even number was found in the given range.

The test cases included assert that the function behaves as expected with the provided example inputs.