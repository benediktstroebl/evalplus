Here's a Python script that contains a function to solve the given problem:
```python
def solve(N):
    binary_str = ''
    total_sum = 0

    while N > 0:
        digit = N % 2
        total_sum += digit
        binary_str = str(digit) + binary_str
        N //= 2

    return f'{total_sum:b}' + binary_str

# Test cases
print(solve(1000))  # Should be: 1
print(solve(150))  # Should be: 110
print(solve(147))  # Should be: 1100
```

The function `solve` uses a while loop to convert the integer `N` to a binary string, and at the same time, it keeps track of the sum of the digits in binary. The sum is accumulated in the `total_sum` variable. The final output is formulated by concatenating the binary representation of the total sum with the binary string representation of the original number `N`. The `f'{total_sum:b}'` formatting is used to convert the `total_sum` to a binary string.