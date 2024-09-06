Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string of the sum of the digits of n converted to binary
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if bin_sum.isdigit() else '0' + bin_sum
```

This script defines a function `solve(n)` that takes in a integer `n` as a parameter, the function converts the integer into a string and sums the value of each digit, then it converts the sum into a binary string and returns it. The function includes a check for the beginning of the binary string to determine if it starts with "0" or not, then returns accordingly.

To use this code, you can simply call the function with a number as follows:
```python
print(solve(147))
```

The output of this call will be:
```
1100
```