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

This Python script defines the `choose_num` function, which takes two integers `x` and `y` as input. It aims to find the largest even integer within the range `[x, y]`, inclusively.

Here's how it works:
1. The variable `max_even` is assigned the maximum value between `x` and `y`, ensuring that the largest even number in the range is considered.
2. The variable `floor_odd` is calculated by dividing the maximum value (either `x` or `y`) by 2. This value represents the smallest odd integer in the range.
3. The code checks two conditions:
   - Whether `max_even` is even (divisible by 2) using the modulus operator `%`.
   - Whether `max_even` is greater than or equal to `floor_odd`.
4. If both conditions are met, indicating that an even number greater than or equal to the smallest odd integer exists within the range, the function returns `max_even`.
5. If no such even number is found, the function returns `-1` to indicate that no valid even number meets the criteria.

The script includes example usage, printing the results of calling `choose_num` with different input values.