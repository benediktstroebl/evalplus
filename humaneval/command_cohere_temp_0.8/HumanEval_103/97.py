Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    bin_str = '-1' if n > m else bin(round((n + m) / 2))[2:]
    return bin_str if bin_str[0] != '-' else '0b' + bin_str

# Example usage
n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
print(rounded_avg(n, m))
```

The function `rounded_avg` calculates the average of the integers between `n` and `m`, inclusive. It then rounds the average to the nearest integer and converts it to binary. If the average is negative, it is prefixed with `0b` to ensure the output is valid binary. The script also handles the case where `n` is greater than `m` by returning `-1` in binary.

To use the script, input two numbers and the resulting binary string will be displayed.