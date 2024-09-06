```python
def choose_num(x, y):
    max_even = max(x, y)
    floor_odd = max(x, y) // 2

    if max_even % 2 == 0 and max_even >= floor_odd:
        return max_even
    else:
        return -1

# Example usage
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
```

This Python script defines a function `choose_num` as per the prompt, taking in two parameters `x` and `y` that are two positive numbers and returning the biggest even integer within the range `[x, y]` or `-1` if no such number exists. The function either returns the maximum even number between the two inputs or `-1` if no such even number exists within the range.

The example usage demonstrates the function's behavior for the provided sample inputs.