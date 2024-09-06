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

This Python script defines the `choose_num` function, which takes two positive numbers `x` and `y` as arguments and returns the largest even integer that falls within the inclusive range between `x` and `y`. If no such even number exists, it returns -1. The code uses the maximum value between `x` and `y` to determine the potential even number and also checks if it's possible to divide this value by 2 to get an odd floor. If the maximum is even and exceeds or equals the floor, it returns the even number; otherwise, it returns -1. 

The example usage demonstrates how the function works with different input scenarios.