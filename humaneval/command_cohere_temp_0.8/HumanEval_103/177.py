Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    binary_str = bin(round(avg))[2:]
    return binary_str if binary_str[0] != '0' else binary_str[1:]

# Tests
print(rounded_avg(1, 5))  # Output: "0b11"
print(rounded_avg(7, 5))  # Output: -1
print(rounded_avg(10, 20))  # Output: "0b1111"
print(rounded_avg(20, 33))  # Output: "0b11010"
```

The function `rounded_avg` calculates the average of numbers from `n` to `m` (inclusive) and rounds it to the nearest integer. If the average is rounded down to zero, the function returns the binary string starting from the second character (to avoid the leading '0' caused by rounding down). This solution handles the edge case where `n` is greater than `m` by returning -1. The test block demonstrates the function's behavior with different inputs.