Here's a Python script that includes a function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    binary_string = bin(round(avg))[2:]
    return binary_string if binary_string.isalpha() else '0b' + binary_string

# Tests
print(rounded_avg(1, 5))  # Output: 0b11
print(rounded_avg(7, 5))  # Output: -1
print(rounded_avg(10, 20))  # Output: 0b1111
print(rounded_avg(20, 33))  # Output: 0b11010
```

The function `rounded_avg(n, m)` first calculates the average of the integers from `n` to `m` (inclusive), rounding it to the nearest integer. It then converts the integer to a binary string. If the binary string is not alphanumeric, it prepends a '0b' to ensure the output is a valid binary string. Finally, it returns the binary string if `n` is not greater than `m`, and -1 if `n` is greater than `m`. 

The test code prints the output of the `rounded_avg` function for different input values and verifies the correctness of the function.