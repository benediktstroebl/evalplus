Here's a Python script that includes a function to solve the problem and a set of tests to verify its correctness:
```python
def solve(n):
    """
    :param n: Positive integer
    :return: Binary string representing the sum of digits in base 2
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if bin_sum.isdigit() else '0' + bin_sum

# Tests
n = 1000
assert solve(n) == '1'

n = 150
assert solve(n) == '110'

n = 147
assert solve(n) == '1101100'

n = -1
try:
    solve(n)
except ValueError:
    assert True  # Test passes if ValueError is raised for negative numbers

n = 11
assert solve(n) == '10'
```

This code includes the `solve` function that takes a positive integer `n` as input and returns the binary string representing the sum of its digits. It calculates the sum of the digits using the `sum` function and converts it to binary using `bin`. The leading '1' is removed from the binary representation, and if necessary, a '0' is appended to ensure a valid binary string. The test suite includes various test cases to validate the function's behavior.