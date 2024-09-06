Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of its digits.
    """
    total_sum = sum(map(int, str(n)))
    return format(total_sum, 'b')
```

This function uses Python's built-in `format` to convert the integer `total_sum` to a binary string. The sum is calculated by summing the digits of the integer `n` using `map(int, str(n))`, converting the decimal digits of `n` to individual integers, adding them up, and then converting the result back to a binary string.

To test this function, you can call it with any integer between 0 and 10000 and compare the output with the expected binary representation of the sum of its digits. Here is an example of usage:
```python
# Test the function with a sample input
print(solve(147))  # Expected output: 1100
print(solve(150))  # Expected output: 110
print(solve(1000))  # Expected output: 1
```

This will output:
```bash
1100
110
1
```

This shows the correct conversion of the integer to a binary string representing the sum of its digits.