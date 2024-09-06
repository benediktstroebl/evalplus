```python
def choose_num(x, y):
    max_even = -1
    for num in range(x, y + 1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even if max_even != -1 else -1

# Test Cases
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(2, 4) == 4
```

This Python script defines the `choose_num` function, which takes two positive numbers `x` and `y` as input and returns the largest even integer that falls within the range `[x, y]`, inclusive. If no such number exists, it returns -1. The function uses a loop to iterate through the integers between `x` and `y` (inclusive) and identifies the largest even number within this range, updating the `max_even` variable as necessary. The final result is returned, which is either the largest even number found (`max_even`) or -1 if no such number is in the range. The test cases confirm that the function produces the expected outputs for various scenarios.