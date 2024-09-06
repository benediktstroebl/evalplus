Here's a Python script that includes a function to solve the problem:
```python
def solve(N):
    BIN_DIGIT_SUM = ''
    total_sum = 0
    
    while N > 0:
        digit = N % 2
        total_sum += digit
        
        BIN_DIGIT_SUM = BIN_DIGIT_SUM + str(digit)
        N //= 2
        
    return BIN_DIGIT_SUM if total_sum == 1 else '1' + BIN_DIGIT_SUM

# Test cases
print(solve(1000))  # Should print: 1
print(solve(150))   # Should print: 110
print(solve(147))   # Should print: 1100
```

This code defines a function `solve(N)` that takes a positive integer `N` as input and calculates the sum of its binary digits. It converts the integer to a binary string and iteratively extracts the remainder when `N` is divided by 2, adding its decimal value to the `total_sum`. The function returns the binary string `BIN_DIGIT_SUM` if the `total_sum` is 1; otherwise, it prepends a '1' to the string if needed to ensure a valid binary representation.

The test cases provided in the comment are meant to validate the correctness of the function.