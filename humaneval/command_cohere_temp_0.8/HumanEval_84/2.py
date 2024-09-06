Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string of the sum of the digits of n
    """
    total_sum = 0
    num = str(n)
    for digit in num:
        total_sum += int(digit)
    
    bin_total = bin(total_sum)[2:]
    return bin_total

# Test cases
print(solve(1000) == '1')
print(solve(150) == '110')
print(solve(147) == '1101100')
```

The `solve` function takes an integer `n` as its argument and returns the binary string of the sum of its digits. It first converts the integer to a string `num` and then loops through each digit in `num`. It adds each digit to `total_sum`, which tracks the sum of the digits in decimal. After the loop, it converts `total_sum` to a binary string and returns the result.