Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of digits of n
    """
    total_sum = 0
    for digit in str(n):
        total_sum += int(digit)
    return format(total_sum, 'b')
```

This function loops through each digit in the decimal representation of `n`, summing them, and then converts the total sum back to a binary string, returning the result as described in the prompt.