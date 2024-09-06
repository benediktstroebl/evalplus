Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    bin_str = "{0:b}".format(n)
    sum_bin = bin_str.count('1')
    return f"{sum_bin}"
```

The function `solve` takes a positive integer `n` as its argument and returns the total sum of its digits in binary. It converts the integer `n` to a binary string using the format specification `{0:b}`. The expression `bin_str.count('1')` calculates the count of occurrences of the digit '1' in the binary string, which corresponds to the sum of digits in binary. Finally, it returns the sum of the binary representation as a binary string itself.

The code above provides an efficient solution that adheres to the specified constraints. It does not require any additional imports and is standalone, making it conducive to inclusion in other projects or tests.