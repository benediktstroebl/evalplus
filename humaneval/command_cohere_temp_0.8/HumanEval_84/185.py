Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    bin_str = '{0:b}'.format(n)
    sum_list = [int(i) for i in bin_str]
    return '{0:b}'.format(sum(sum_list))
```
This Python script defines a function `solve(n)` that takes an integer `n` as input and returns the binary string equivalent of the total sum of its digits. The function first converts the integer `n` to a binary string using the `format` method with a base-2 exponentiation (`{0:b}`.format(n)). It then creates a list from the binary string, converting each element to an integer. The function then sums these integer values and converts the result back to a binary string, returning it as the output.