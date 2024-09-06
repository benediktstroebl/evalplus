Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string sum of digits of N
    """
    total_sum = 0
    tmp_n = n
    while tmp_n > 0:
        digit = tmp_n % 2
        total_sum += digit
        tmp_n //= 2
    # Convert to string and append leading zero if necessary
    return str(total_sum) + '0' * (len(str(n)) - len(str(total_sum)))
```

This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It uses a while loop to iterate through the digits of `n` in reverse, converting each digit to binary and adding it to the total sum. The function then converts the binary sum to a string and appends any necessary leading zeros to match the length of the input number `n`.