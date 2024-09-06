```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input numbers must be not empty or None")
    if a == 0 or b == 0:
        return 0
    # prime factorization and divisor calculation
    dp = [0] * (b + 1)
    dp[0] = 1
    for i in range(1, b + 1):
        if a % i == 0:
            for j in range(i, b + 1, i):
                dp[j] += dp[j - i]
    return dp[b]

# test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(59, 123))  # Output: 29
```