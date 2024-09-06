Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary
    :return: Binary string summing up to the total of digits in base 10
    """
    bin_str = bin(n)[2:]
    if not bin_str:
        return '0'
    else:
        return bin_str.count('1') % 2 == 0 and str(bin_str.count('1')) or '1'

# Test cases
print(solve(1000))
print(solve(150))
print(solve(147))
```

The function `solve` takes an integer `n` as input and returns a binary string that sums up to the total of its digits in base 10. This is achieved by first converting the integer to a binary string and then counting the number of '1's in the string. If the count of '1's is odd, then the function returns `1`, otherwise, it returns the count of '1's in binary. The test cases demonstrate the function's behavior for the specified problem.