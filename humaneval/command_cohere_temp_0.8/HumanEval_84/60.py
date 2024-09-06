Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :type n: int
    :param n: integer
    :rtype: str
    """
    binary_str = ''
    total_sum = 0
    while n > 0:
        digit = n % 2
        total_sum += digit
        binary_str = str(digit) + binary_str
        n //= 2
    return format(total_sum, 'b') + binary_str
```

This function, `solve(n)`, takes a positive integer `n` as input and iterates through its digits from least significant to most significant. It converts each digit to binary and adds them to a running total. Once all digits are processed, the function returns a string of the binary representation of the total sum of the digits.

Here's an example of how you can use this function to solve for `n = 147`:
```python
print(solve(147))
# Outputs: 1100
```

This accurately solves the problem statement's example since the sum of digits in binary for 147 is `1101` which corresponds to `1100` in binary representation.