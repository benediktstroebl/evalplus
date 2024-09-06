Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    bin_sum = 0
    while n > 0:
        digit = n % 10
        bin_sum += digit
        n = n // 10
    return format(bin_sum, 'b')
```
This script defines a function `solve(n)` that calculates the sum of digits of the given integer `n` and returns it in binary format. It uses a `while` loop to iterate through the digits of `n` and accumulates the sum in the `bin_sum` variable. Finally, the function formats the `bin_sum` in binary using `format` and returns the result.