Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :type n: int
    :param n: Should be a positive integer
    :return: A string of binary number
    """
    # Convert the decimal number to a binary string
    binary_representation = bin(n)[2:]
    # Convert each digit in the binary string to a decimal number
    decimal_digits = [int(digit) for digit in binary_representation]
    # Add up the decimal numbers to get the total sum
    total_sum = sum(decimal_digits)
    return bin(total_sum)[2:]
```

This script defines a function `solve(n)` that takes in a positive integer `n` as input and calculates the sum of its binary digits. It converts the input number `n` to a string of binary digits, converts each digit to a decimal number, sums up those decimal numbers, and then converts the total sum back to a string of binary digits. This result is then returned as the final output.