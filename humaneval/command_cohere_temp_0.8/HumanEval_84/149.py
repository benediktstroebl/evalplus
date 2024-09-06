Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be transformed to binary sum of digits
    :return: String binary representation of sum of digits of n
    """
    total_sum = 0
    for digit in str(n):
        total_sum += int(digit)
    return format(total_sum, 'b')
```

The function `solve` iterates through each digit in the passed integer `n`, converts each digit to an integer to add it to the `total_sum`, and then converts the `total_sum` to a binary string for output. This code block effectively solves the given problem and should produce the desired output.