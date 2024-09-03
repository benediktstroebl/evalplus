Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Positive integer N
    :return: Binary string of the sum of digits of N
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if bin_sum.isdigit() else '0' + bin_sum
```

This script defines a function `solve(n)` that takes a positive integer `n` as input and calculates the sum of its digits in binary representation, returning it as a binary string. It achieves this by first summing the individual digits of the decimal representation of `n`, then converting the sum into a binary number using `bin`, and finally trimming off the leading '0b' and any non-digit characters from the binary representation. The result is returned as a binary string.

The unit tests for this function are not included as they are stated as given code. You can add your own tests to verify the correctness of the function. Here's an example of how you may add a test: 
```python
# Test the solve function
def test_solve():
    assert solve(0) == '0'
    assert solve(1) == '1'
    assert solve(10) == '10'
    assert solve(5142) == '10010010'
    assert solve(123) == '11011'
    assert solve(15) == '110'
    assert solve(147) == '1100'
```