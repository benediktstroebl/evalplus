Here's a Python script that includes a function to solve the problem and a set of tests to verify its correctness:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string sum of decimal representation of n
    """
    return str(bin(sum([int(d) for d in str(n)]))[2:])

# Tests
n = 1000
assert solve(n) == "1"

n = 150
assert solve(n) == "110"

n = 147
assert solve(n) == "1100"

n = 1001
assert solve(n) == "10"

n = 11
assert solve(n) == "1011"

n = 299
assert solve(n) == "11011"

n = 7
assert solve(n) == "111"
```

The function `solve(n)` takes a positive integer `n` as input and returns the binary string that is the sum of its digits. It does this by first converting the number to a string, iterating over each digit, summing them, converting the sum to a binary number, and returning the binary representation.

The test section includes a set of test cases that validate the correctness of the `solve()` function. Each test case checks if the returned binary string matches the expected result for the given positive integer `n`.