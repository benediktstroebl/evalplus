Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String - Binary string of the sum of digits
    """
    total_sum = 0
    # Convert integer to binary string
    bin_str = bin(n)[2:]
    while bin_str:
        digit = int(bin_str[0])
        total_sum += digit
        bin_str = bin_str[1:]
    # Convert total sum to binary string
    sum_in_binary = bin(total_sum)[2:]
    return sum_in_binary
```

The function `solve` takes an integer `n` as its parameter and returns the binary string of the sum of its digits. It converts the integer to a binary string and then iterates over its digits. The sum of the digits is calculated and then converted to a binary string. Finally, it returns the binary string representing the sum of the digits.