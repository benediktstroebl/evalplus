Here's a Python script that includes a function to solve the given problem:
```python
def solve(N):
    BIN_DIGIT_SUM = '0'
    DIG_COUNT = 0

    while N > 0:
        DIG_COUNT += 1
        N //= 10

    while DIG_COUNT > 0:
        BIN_DIGIT_SUM = BIN_DIGIT_SUM * 2 + '1'
        DIG_COUNT -= 1

    return BIN_DIGIT_SUM

# Test Cases
print(solve(1000)) # Should output: 1
print(solve(150))  # Should output: 110
print(solve(147))  # Should output: 1100
```

This script defines a function `solve` that takes a positive integer `N` as input and calculates the total sum of its digits in binary. It iterates through the digits of `N` and counts the number of digits, then iterates through that count and builds the binary string representation of the sum. The function returns a binary string representing the sum of the digits.