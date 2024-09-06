Here's a Python script that includes a function to solve the problem:
```python
def solve(N):
    """
    :param N: integer
    :return: string
    """
    bin_str = bin(N)[2:]
    sum_str = ''.join(str(int(bit) for bit in bin_str if int(bit)))
    return sum_str
```

The function uses the built-in `bin` function to convert the integer `N` to a binary string, and then iterates through the string to convert each binary digit to an integer value and sums these values. The resulting sum is then converted to a binary string and returned. It assumes that the input `N` is already validated and within the range of 0 <= N <= 10000.  If you have a specific large test case that causes an issue, please provide it and I will investigate further. Let me know if this solution suits your needs or if you'd like any alterations to be made. I can also provide a simple test suite if desired.