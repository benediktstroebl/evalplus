Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string of the sum of its digits.
    """
    total_sum = 0
    num = str(n)
    for digit in num:
        total_sum += int(digit)
    
    # Convert total sum to binary string
    binary_str = bin(total_sum)[2:]
    return binary_str

# Test Cases
print(solve(1000))  # Should output: 1
print(solve(150))   # Should output: 110
print(solve(147))   # Should output: 1100
```

This code defines a function `solve` that takes an integer `n` as its parameter and calculates the sum of its digits in binary. It does this by first iterating through each digit in the decimal number, summing them, and then converting the total sum to a binary string. The provided test cases demonstrate its usage and output.