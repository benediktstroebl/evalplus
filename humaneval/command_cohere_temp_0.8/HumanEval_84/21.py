Here's a Python script that contains a function to solve the given problem:
```python
def solve(N):
    """
    :param N: integer
    :return: string
    """
    bin_str = bin(N)[2:]
    return bin_str.replace('0', '').strip('1')
```

The `solve` function takes an integer `N` as its input. It converts the integer to a binary string and then removes '0's and leading '1's. The resulting binary string is then returned, representing the sum of digits in binary form. 

For example, given the integer `N = 1000`, the function would return `"1"`, as the sum of its digits in binary is `1`. 

This solution leverages Python's built-in `bin` function to efficiently convert the given integer to a binary string and then simplifies the string to capture the sum of its binary digits.