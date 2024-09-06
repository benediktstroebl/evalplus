Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    """
    :param n: Integer to be transformed to binary sum of digits
    :return: String binary representation of sum of digits of n
    """
    return '{:b}'.format(sum(map(int, str(n))))
```
This script provides the `solve` function, which accepts a positive integer `n` as input and computes the binary representation of the total number of its digits. The `format` method is used in conjunction with `{:b}` to apply the binary format specifier to the result of the `sum` function and map it to an integer. This approach allows for an efficient computation of the required result, while also being straightforward and easily understandable. The function is designed to work correctly for values of `n` within the specified range of 0 to 10,000.