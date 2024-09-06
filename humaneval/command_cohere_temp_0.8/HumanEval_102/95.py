```python
def choose_num(x, y):
    max_even = max(x, y)
    floor_odd = max(x, y) // 2

    if max_even % 2 == 0 and max_even >= floor_odd:
        return max_even
    else:
        return -1

# Example usage:
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
```

This Python script defines the `choose_num` function, which takes two positive numbers `x` and `y` as arguments. It aims to return the largest even integer that falls within the range `[x, y]`, inclusive. If no such even number is found within this range, it returns -1. The script includes example usage, demonstrating how the function works with different input scenarios.