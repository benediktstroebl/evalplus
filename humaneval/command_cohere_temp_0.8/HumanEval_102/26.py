```python
def choose_num(x, y):
    max_even = -1
    temp_num = x
    while temp_num <= y:
        if temp_num % 2 == 0:
            max_even = temp_num
        temp_num += 1
    return max_even if max_even != -1 else -1

# Example usage
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
```

This Python script defines the `choose_num` function, which takes two positive numbers `x` and `y` as inputs and searches for the largest even integer that falls within the inclusive range `[x, y]`. The function iterates through the range, checking if each number is even. The largest even number found is returned, or `-1` if no such number is in the range. 

The example usage demonstrates how the function works for different input scenarios.